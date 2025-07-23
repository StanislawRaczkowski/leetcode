class Solution:
    def maxArea(self, height: List[int]) -> int:
        Area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            Temporary = (min(height[right], height[left])*(right-left))
            if Temporary > Area:
                Area = Temporary
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return Area

        # Area = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         Temporary = min(height[j], height[i]) * (j-i)
        #         if Temporary > Area:
        #             Area = Temporary
        # return Area
