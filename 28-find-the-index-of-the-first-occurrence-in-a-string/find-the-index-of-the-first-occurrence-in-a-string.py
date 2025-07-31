class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay = list(haystack)
        n = len(needle)
        for char in range(len(hay)):
            left = char
            right = char + n
            if haystack[left:right] == needle:
                return left
        return -1