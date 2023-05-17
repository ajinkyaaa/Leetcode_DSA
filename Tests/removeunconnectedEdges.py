"""
[[1,0,0,0,0,0],
 [0,1,0,1,1,1],
 [0,0,1,0,1,0],
 [1,1,0,0,1,0],
 [1,0,1,1,0,0],
 [1,0,0,0,0,1]]

ROWS = len(rows)
COLS = len(cols)

rows => 1, ROWS-1
cols = 1, COLS-1

DFS AT EACH NODE , if it reaches end and 1 then return True,else return False => if false we cahnge to 0

""" 

grid = [[1,0,0,0,0,0],
        [0,1,0,1,1,1],
        [0,0,1,0,1,0],
        [1,1,0,0,1,0],
        [1,0,1,1,0,0],
        [1,0,0,0,0,1]]

def removeunconnected(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    visited = []
    def dfs(row,col):
        if ((row,col)) in visited:
            return False
        visited.append((row,col))
        if row == ROWS-1 or col == COLS-1 or row == 0 or col==0:
            visited.remove((row,col))
            if grid[row][col] == 1:
                return True
            else:
                return False
        
        if grid[row][col] == 0:
            return False
        
        if row > 0:
            left = dfs(row-1,col)
        if row < ROWS-1:
            right = dfs(row+1,col)
        if col > 0:
            top = dfs(row,col-1)
        if col < COLS -1:
            bot = dfs(row,col+1)
        
        visited.remove((row,col))
        return left or right or top or bot


    for row in range(1,ROWS-1):
        for col in range(1,COLS-1):
            if grid[row][col]== 1:
                if (row,col) not in visited:
                    
                
                    if dfs(row,col) == False:
                        grid[row][col] = 0
                
                #visited.remove((row,col))
    return grid

"""
[[1, 0, 0, 0, 0, 0], 
[0, 0, 0, 1, 1, 1],
[0, 0, 0, 0, 1, 0], 
[1, 1, 0, 0, 1, 0],
[1, 0, 0, 0, 0, 0], 
[1, 0, 0, 0, 0, 1]]

"""

print(removeunconnected(grid))



