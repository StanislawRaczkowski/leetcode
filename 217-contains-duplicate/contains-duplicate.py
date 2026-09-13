class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Third one, hash map:
        used = {}
        for i in nums:
            if i in used and used[i] >= 1:
                return True
            used[i] = used.get(i, 0) + 1
        return False

        # Second attempt, working even better:
        # s = set()
        # for i in nums:
        #     if i in s:
        #         return True
        #     s.add(i)
        # return False

        # That was first idea, which worked:
        # s = set(nums)
        # nums2 = list(s)
        # print(nums2)
        # if sorted(nums) == sorted(nums2):
        #     return False
        # else:
        #     return True