class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        k = nums.index(max(nums))
        leftarr = nums[:k+1]
        rightarr = nums[k+1:]
        print(leftarr, rightarr)
        left = 0
        right = len(rightarr) - 1
        while left <= right:
            mid = (left+right)//2
            if rightarr[mid] == target:
                return mid + len(leftarr)
            if rightarr[mid] < target:
                left = mid + 1
            else: 
                right = mid - 1
        lefte = 0
        righte = len(leftarr) - 1
        while lefte <= righte:
            mid = (lefte+righte)//2
            if leftarr[mid] == target:
                return mid 
            if leftarr[mid] < target:
                lefte = mid + 1
            else: 
                righte = mid - 1
        return -1

            
        
