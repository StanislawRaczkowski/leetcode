class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return n
        Now, Prev = 1, 1
        # Now is a current step, Prev is a previous step solutions
        for i in range(2,n+1):
            temporary = Now
            Now = Prev + Now
            Prev = temporary
        return Now


# FIrst try, TLE however:
# class Solution:

#     # number of solutions is s
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         else:
#             s = self.climbStairs(n-1) + self.climbStairs(n-2)
#         return s
