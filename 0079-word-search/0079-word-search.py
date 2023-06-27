class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [[0] * m for _ in range(n)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y, idx):
            if idx == len(word) - 1 and board[x][y] == word[idx]:
                return True
            if board[x][y] != word[idx]:
                return False

            visited[x][y] = 1
            for dx, dy in directions:
                nx, ny =  x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                    if dfs(nx, ny, idx + 1):
                        return True
            visited[x][y] = 0
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and  dfs(i, j, 0):
                    return True
        return False

