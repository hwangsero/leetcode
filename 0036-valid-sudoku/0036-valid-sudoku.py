class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 10
        rows = [[0] * N for _ in range (N)]
        cols = [[0] * N for _ in range (N)]
        boxes = [[0] * N for _ in range (N)]

        for x in range(len(board)):
            for y in range(len(board[x])):
                val = board[x][y]
                if val == '.':
                    continue
                int_val = int(board[x][y])
                
                if rows[x][int_val] == 1:
                    return False
                rows[x][int_val] = 1

                if cols[y][int_val] == 1:
                    return False
                cols[y][int_val] = 1

                if boxes[x // 3 * 3 + y // 3][int_val] == 1:
                    return False
                boxes[x // 3 * 3 + y // 3][int_val] = 1

        return True
