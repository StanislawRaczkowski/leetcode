class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if s == s[::-1]:
        #     return s
        # palindrome_list = []
        # temporary = []
        # Pali = list(s)
        # for i in range(len(Pali)):
        #     for j in range(i, len(Pali)):
        #         potential = ''.join(Pali[i:j+1])
        #         if potential == potential[::-1]:
        #             palindrome_list.append(potential)
        # longest = max(palindrome_list, key=len)

        # return longest
        # Pierwsza próba, TLE niestety
        pal = list(s)
        start = 0
        end = 0
        for i in range(len(pal)):
            l,r = i, i
            while l >= 0 and r < len(pal) and pal[l] == pal[r]:
                if (r - l) > (end - start):
                    start, end = l, r
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(pal) and pal[l] == pal[r]:
                if (r - l) > (end - start):
                    start, end = l, r
                l -= 1
                r += 1

        return ''.join(pal[start:end + 1])



