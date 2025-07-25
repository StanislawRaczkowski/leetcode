# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         n = len(nums)
#         result = nums[0] + nums[1] + nums[2]
#         for i in range(n-2):
#             left = i + 1
#             right = n - 1
#             while left < right:
#                 print(result)
#                 s = (nums[i] + nums[right] + nums[left]) 
#                 if s == target:
#                     return s
#                 else:
#                     if s < target:
#                         left += 1
#                     elif s > target:
#                         right -= 1
#                     if abs(target - s) < abs(target - result):
#                         result = s
#         return result
import bisect

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = float('inf')
        best_diff = float('inf')

        # Przechodzimy po parach i próbujemy dobrać trzecią liczbę przybliżoną
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                pair_sum = nums[i] + nums[j]
                third_needed = target - pair_sum

                # Szukamy najbliższego kandydata za pomocą bisect
                idx = bisect.bisect_left(nums, third_needed, j + 1)
                for k in [idx - 1, idx]:  # sprawdź sąsiadów
                    if j < k < n:
                        s = pair_sum + nums[k]
                        if abs(target - s) < best_diff:
                            best = s
                            best_diff = abs(target - s)
        return best



                