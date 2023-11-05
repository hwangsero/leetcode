class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while i >= 0:
            if s[i] != " ":
                break
            i -= 1
        length = 0
        while i >= 0:
            if s[i] == " ":
                break
            length += 1
            i -= 1
        return length
        