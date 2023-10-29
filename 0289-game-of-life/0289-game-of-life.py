class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = [0, -1, 1]
        m, n = len(board), len(board[0])
        check_board = [[0] * n for _ in range(m)]


        def check_cell(x, y):
            alive_cnt = 0
            for dx in d:
                for dy in d:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 1:
                        alive_cnt += 1
            if board[x][y] == 0 and alive_cnt == 3:
                check_board[x][y] = 1
            elif board[x][y] == 1 and alive_cnt in [2, 3]:
                check_board[x][y] = 1


        for x in range(m):
            for y in range(n):
                check_cell(x, y)

        board[:] = check_board[:]