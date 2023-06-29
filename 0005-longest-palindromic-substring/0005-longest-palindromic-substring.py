class Solution:


    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for length in range(2, n):
            for start in range(0, n - length):
                if s[start] == s[start + length] and dp[start + 1][start + length - 1]:
                    dp[start][start + length] = True
                    ans = [start, start + length]
        i, j = ans
        return s[i:j + 1]


                