class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = nums[0] + nums[1] + nums[2]
        if result == target:
            return result
        for i in range(n-2):
            left = i + 1
            right = n - 1
            while left < right:
                print(result)
                s = (nums[i] + nums[right] + nums[left]) 
                if s == target:
                    return s
                else:
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    if abs(target - s) < abs(target - result):
                        result = s
        return result




                