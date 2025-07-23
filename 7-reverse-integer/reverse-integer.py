class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        z = str(y)
        if x < 0:
            a = int("-"+z[::-1])
        else:
            a = int(z[::-1])
        if a > (pow(2, 31) - 1):
            return 0
        if a < (pow(-2, 31)):
            return 0
        return a