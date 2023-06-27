class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [[0] * m for _ in range(n)]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def dfs(x, y, idx):
            if idx == len(word) - 1 and board[x][y] == word[idx]:
                return True
            if board[x][y] != word[idx]:
                return False

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (nx >= 0 and nx < n and ny >= 0 and ny < m and visited[nx][ny] == 0):
                    
                    visited[nx][ny] = 1
                    if dfs(nx, ny, idx + 1):
                        return True
                    visited[nx][ny] = 0
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited = [[0] * m for _ in range(n)]
                    visited[i][j] = 1
                    if dfs(i, j, 0):
                        return True
        return False
