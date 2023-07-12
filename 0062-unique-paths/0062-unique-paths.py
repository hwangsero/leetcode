class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        d = [[1] * n for _ in range(m)]
        for x in range(1, m):
            for y in range(1, n):
                d[x][y] = d[x - 1][y] + d[x][y - 1]

        return d[m - 1][n - 1]

