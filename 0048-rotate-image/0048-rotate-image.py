class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = m  = len(matrix)
        cnt = 0
        while m > 0:
            for y in range(cnt, n-cnt-1):
                x = cnt
                for i in range(5):
                    tmp = matrix[x][y]
                    if i > 0:
                        matrix[x][y] = pre_num
                    pre_num = tmp
                    x, y = y, n-x-1
            m -= 2
            cnt += 1
        return matrix
