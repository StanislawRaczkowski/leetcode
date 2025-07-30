class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], []
        def Back(close, opene):
            if len(sol) == 2*n:
                ans.append(''.join(sol))
                return
            if opene < n:
                sol.append('(')
                Back(close, opene + 1)
                sol.pop()
            if opene > close:
                sol.append(')')
                Back(close + 1, opene)
                sol.pop()
        Back(0, 0)
        return ans

        # Solution = []
        # Brackets = {")": "("}
        # first = n*"("+n*")"
        # # Solution.append(first)
        # print(Solution)
        # string = list(first)
        # left = n - 1
        # right = n
        # for i in range(len(string)):
            
        #     while (left != 0 or right != (2*n) - 1) and left < right:

        # return Solution