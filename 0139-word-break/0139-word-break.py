class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.words = set()
        for word in wordDict:
            self.words.add(word)

        self.d = {}

        return self.check_word(s)
        

    def check_word(self, s: str):
        if s == '':
            return True

        if s in self.d:
            return self.d[s]

        result = False
        for i in range(1, len(s) + 1):
            cur_word = s[:i]
            if cur_word in self.words:
                if self.check_word(s[i:]):
                    result = True
        self.d[s] = result
        return result
