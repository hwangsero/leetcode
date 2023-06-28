class Solution:
    def numDecodings(self, s: str) -> int:
        self.s = s
        self.d = [-1] * len(s)
        return self.check_decoding(0)


    def check_decoding(self, idx):
        if idx == len(self.s):
            return 1
        if self.s[idx] == '0':
            return 0
        if self.d[idx] != -1:
            return self.d[idx]

        ans = 0
        if 1 <= int(self.s[idx]) <= 26:
            ans += self.check_decoding(idx + 1)
        
        if idx + 1 < len(self.s) and 1 <= int(self.s[idx:idx + 2]) <= 26:
            ans += self.check_decoding(idx + 2)
        self.d[idx] = ans
        return ans


        
