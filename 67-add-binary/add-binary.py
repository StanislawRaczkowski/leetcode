class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sol = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            sol.append(str(carry % 2))
            carry = carry // 2
        return ''.join(reversed(sol))
            

  
    #    alist = a.split()
    #     blist = b.split()
    #     for i in alist.reverse():
    #         for j in blist.reverse():
    #             alist[i] = alist[i] + blist[j]
    #             if  
        # c = a + b
        # clist1 = c.split()
        # clist = clist1.reverse()
        # for i in clist:
        #     if clist[i] == 0 or clist[i] == 1:
        #         continue
        #     else:
        #         clist[i] = 0
        #         if clist[i+1] == False:
        #             clist.append(1)
        #         else:
        #             clist[i+1] = clist[i+1] + 1
        # clist.join()
        # return clist

