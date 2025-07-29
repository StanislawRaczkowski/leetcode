class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        solution = []
        for i in range(n-1):
            for j in range(i+1, n-1):
                if j <= i:
                    pass
                else:
                    left = j + 1
                    right = n - 1
                    while left < right:
                        diff = target - nums[i] - nums[j]
                        if nums[left] + nums[right] == diff and (sorted([nums[i], nums[j], nums[right], nums[left]])) not in solution:
                            solution.append(sorted([nums[i], nums[j], nums[right], nums[left]]))
                            left += 1
                            right -= 1
                        else:
                            if nums[i] + nums[j] + nums[right] + nums[left] < target:
                                left += 1
                            else:
                                right -= 1
                            
        return solution
# nums[i] + nums[j] + nums[right] + nums[left]

