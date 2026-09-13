class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        instlist = []
        least = -1
        for i in range(n):
            maxi = max(nums[0:i+1])
            mini = min(nums[i:n+1])
            diff = maxi - mini
            instlist.append(diff)
            if diff <= k and min(instlist) >= diff:
                least = diff
                return instlist.index(least)
        return least


        # print(instlist)
        # if least == -1:
        #     return -1
        # else:
        #     return instlist.index(least)


        # print(instlist)
        # least = min(instlist)
        # idx = instlist.index(least)
        # if least <= k:
        #     return idx
        # else:
        #     return -1