class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lettuce = list(s)

        rows = [[] for i in range(numRows)]
        nowrow = 0
        direction = False
        print(rows)
        if numRows == 1:
            return s
        for i in lettuce:
            rows[nowrow].append(i)
            if nowrow == 0 or nowrow == numRows -1:
                direction = not direction
            if direction == True:
                nowrow += 1
            else:
                nowrow -= 1
        last = sum(rows, [])
        print(last)
        return ''.join(last)
            



        # lettuce = list(s)
        # step = 2*numRows + 1
        # conv = []
        # for j in lettuce:
        #     print(lettuce.index(j))
        #     if lettuce.index(j) % step == 0:
        #         conv.append(j)
        #     else:
        #         step += 1
            # if  lettuce.index(j) > len(s):
            #     break
            # if int(index(j)) % step == 0:
            #     conv.append() 
        #Not working
        # return ''.join(conv)
            
        
