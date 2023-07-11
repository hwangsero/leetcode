class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        ans = []
        m, n = len(matrix), len(matrix[0])
        x, y = 0, 0
        dir = 0
        turn_flag = False
        EXIST_FLAG = 200

        while True:
            if matrix[x][y] != EXIST_FLAG:
                ans.append(matrix[x][y])
            matrix[x][y] = EXIST_FLAG

            nx, ny = x + dx[dir], y + dy[dir]
            if (nx < 0 or nx >= m or ny < 0 or ny >= n
                or matrix[nx][ny] == EXIST_FLAG):
                if turn_flag:
                    return ans
                elif not turn_flag:
                    turn_flag = True
                    dir = (dir + 1) % 4
            else:
                x, y = nx, ny
                turn_flag = False



