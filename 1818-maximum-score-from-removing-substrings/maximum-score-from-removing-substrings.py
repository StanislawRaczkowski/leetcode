class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        if y > x:
            first = "ba"
            prim = y
            second = "ab"
            sec = x
        else:
            first = "ab"
            prim = x
            second = "ba"
            sec = y
        total = 0
        for i in s:
            stack.append(i)
            if len(stack) >= 2 and stack[-2] + stack[-1] == first:
                stack.pop()
                stack.pop()
                total = total + prim
        stack2 = []
        for j in stack:
            stack2.append(j)
            if len(stack2) >= 2 and stack2[-2] + stack2[-1] == second:
                stack2.pop()
                stack2.pop()
                total = total + sec
        return total
                



       

        # for i in range(len(s)-1):
        #     if s[i:i+2] == "ab":
        #         x_count += 1
        #         s.replace("ab", "", 1)
        #         i = 0
        # x_total = x * x_count
        # for j in range(len(s) - 1):
        #     if s[j:j+2] == "ba":
        #         y_count += 1
        #         s.replace("ba", "", 1)
        #         j = 0 

        # y_total = y * y_count
        # return max(x_total, y_total)

