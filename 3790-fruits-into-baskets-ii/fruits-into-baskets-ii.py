class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        baskets = baskets.copy()
        counter = len(fruits)
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i]:
                    baskets[j] = 0
                    counter -= 1
                    break
        return counter
            # left = 0
            # right = n - 1
            # while left <= right:
            #     mid = (left + right) // 2
            #     if baskets[mid] >= fruits[i]:
            #         baskets.pop(mid)
            #         counter =- 1
            #     if baskets[mid] < fruits[i]:

                
