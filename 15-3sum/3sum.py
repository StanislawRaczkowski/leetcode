class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                s = nums[right] + nums[left] + nums[i]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result


        # Still too much complexity, but O(n^2) at least
        # lettuce = {} #key = value
        # solution = []
        # result = []
        # for i in range(len(sorted(nums))):
        #     target = nums[i]
        #     for j in range(len(sorted(nums))):
        #         if j == i:
        #             pass
        #         else:
        #             wanted = 0 - nums[j] - nums[i]
        #             if wanted in lettuce and wanted in nums and nums.index(wanted) != j and nums.index(wanted) != i and (sorted([nums[j], nums[i], wanted])) not in solution:
        #                 solution.append(sorted([nums[j], nums[i], wanted]))
        #             lettuce[nums[j]] = j
        # return solution

        #Too much complexity
        # solutions = []
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j == i: 
        #             pass
        #         else:
        #             for k in range(len(nums)):
        #                 if k != j and k != i:
        #                     if nums[k] + nums[j] + nums[i] == 0 and (sorted([nums[k], nums[j], nums[i]]) in solutions) is False:
        #                         temp = sorted([nums[k], nums[j], nums[i]])
        #                         solutions.append(temp)
        #                 else: 
        #                     pass
        # # tup = tuple(solutions)
        # # sol = list(tup)
        # return solutions
