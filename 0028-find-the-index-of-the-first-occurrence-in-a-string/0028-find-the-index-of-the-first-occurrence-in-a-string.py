class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for idx in range(len(haystack) - len(needle) + 1):
            c = haystack[idx:idx + len(needle)]
            if c == needle:
                return idx
        return -1


       