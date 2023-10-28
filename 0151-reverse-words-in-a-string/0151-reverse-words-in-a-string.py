class Solution:
    def reverseWords(self, s: str) -> str:
        splited = s.strip().split()
        splited.reverse()
        return " ".join(splited)
