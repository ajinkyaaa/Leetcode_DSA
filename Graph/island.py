class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        self.grid = grid
        self.top = 0
        self.bot = ROWS -1
        self.left = 0
        self.right = COLS -1
        noOfIslands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    self.dfs(row,col)
                    noOfIslands += 1
        return noOfIslands

    def dfs(self,row,col):
        if self.grid[row][col] == "1":
            self.grid[row][col] = "0"
        else:
            return
        
        if col < self.right:
            self.dfs(row,col+1)
        if col > self.left:
            self.dfs(row,col-1)
        if row < self.bot:
            self.dfs(row+1,col)
        if row > self.top:
            self.dfs(row-1,col)