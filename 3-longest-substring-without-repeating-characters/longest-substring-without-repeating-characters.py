class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lett = list(s)
        temporary = []
        longest = 0
        # for i in range(len(lett)):
        #     for j in range(len(lett)):
        #         if lett[i] == lett[j]:
        #             temporary = lett[i:j]
        #             i=j
        #             if len(temporary) > len(longest):
        #                 longest = temporary
        # return len(longest)
        #to było pierwsze podejście, nieudane jednakowoż
        for char in s:
            if char in temporary:
                duplicate = temporary.index(char)
                temporary = temporary[duplicate + 1:]
            temporary.append(char)
            longest = max(len(temporary), longest)
        return longest



                



