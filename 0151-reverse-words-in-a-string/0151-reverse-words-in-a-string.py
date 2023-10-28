class Solution:
    def reverseWords(self, s: str) -> str:
        splited = s.strip().split(" ")
        splited.reverse()
        splited = filter(lambda x: x != "", splited)
        print(splited)
        return " ".join(splited)
