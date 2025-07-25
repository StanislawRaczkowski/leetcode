class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target - nums[i]
            print(temp)
            if temp in nums and nums.index(temp) != i:
                return [i, nums.index(temp)]
            
        

        # Brute force
        # solution = []
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j == i:
        #             pass
        #         else:
        #             if nums[j] + nums[i] == target:
        #                 solution = [i, j]
        # return solution