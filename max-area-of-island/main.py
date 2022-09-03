from typing import List 

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    result = 0
    rows  = len(grid) 
    cols  = len(grid[0])
    def dfs(row,col,currArea):
        # check if valid
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return currArea # out of bounds
        
        if grid[row][col] != 1:
            return currArea # either water or visited
        
        # visit the cell
        grid[row][col] = -1
        currArea += 1
        
        # visit all adjacent cells
        currArea = dfs(row+1,col,currArea)
        currArea = dfs(row-1,col,currArea)
        currArea = dfs(row,col+1,currArea)
        currArea = dfs(row,col-1,currArea)
        return currArea
        
    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]
            if cell == 1:
                # start visiting this island
                result = max(result , dfs(row,col, 0))
                
    return result
    


            
                
# https://leetcode.com/problems/max-area-of-island/
if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(maxAreaOfIsland(grid))


    
