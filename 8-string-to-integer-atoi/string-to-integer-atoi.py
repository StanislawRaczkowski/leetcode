class Solution:

    def myAtoi(self, s: str) -> int:
        def to_int32(n):
            return max(-2**31, min(n, 2**31 - 1))  

        lettuce = []
        j = 0
        b = s.strip()
        if b.startswith("-"):
            lettuce.append("-")
            j = 1
        if b.startswith("+"):
            j = 1
        for char in b[j:]:  
            if char.isdigit():
                lettuce.append(char)
            else:
                break
        if lettuce == []:
            lettuce.append("0")
        if lettuce == ["-"] or lettuce == ["+"]:
            return 0
        x = int(''.join(lettuce))
        return to_int32(x)

#Other approaches
        # lettuce = []
        # j = 0 #whitespaces counter
        # p = 0
        # for char in s:
        #     if char == " ":
        #         j = j + 1
        #     else:
        #         break
        # if s.startswith("-"):
        #     lettuce.append("-")
        #     p = 1
        # if s.startswith("+"):
        #     p = 1
        # for char in s[j+p:]:  
        #     if char.isdigit():
        #         lettuce.append(char)
        #     else:
        #         break
        # if lettuce == []:
        #     lettuce.append("0")
        # x = int(''.join(lettuce))
        # return x

        # lettuce = list(s)
        # conv = []
        # if lettuce[0] == "-":
        #     conv.append("-")
        # if lettuce[0] == "+":
        #     pass
        # for i in range(len(lettuce) - 1):
        #     if lettuce[i].isdigit():
        #         conv.append(lettuce[i])
        #     elif lettuce[i] == " ":
        #         pass
        #     else:
        #         break
        # x = ''.join(conv)
        # # if x == '': 
        # #     return 0
        # # else:
        # #     return int(x)
        # return conv