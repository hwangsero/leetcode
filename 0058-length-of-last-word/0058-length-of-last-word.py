class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_len = 0
        for char in reversed(s):
            if char == " " and word_len > 0:
                break
            elif char != " ":
                word_len += 1

        return word_len
