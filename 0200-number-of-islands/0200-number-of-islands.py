class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
        self.grid = grid
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        island_cnt = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == "1":
                    island_cnt += 1
                    self.explore_island(row, col)
        return island_cnt

    def explore_island(self, row, col):
    
        self.grid[row][col] = "-1"
        for d in self.directions:
            nx, ny = row + d[0], col + d[1]
            if (0 <= nx < self.rows and 0 <= ny < self.cols 
                and self.grid[nx][ny] == "1"):
                self.explore_island(nx, ny)
                
        
        
