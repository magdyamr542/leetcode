from typing import List
def orangesRotting(grid: List[List[int]]) -> int:
    currRotten = [] # list of 2d indexes of the rotten oranges that are being processed now
    result = 0 # the min num of minutes to wait before all fresh oranges are rotten
    rows = len(grid)
    cols = len(grid[0])
    numFresh = 0
    
    # get the initiall empty rotten
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                currRotten.append([row,col])
            elif grid[row][col] == 1:
                numFresh += 1
    
    # keep processing all current rotten oranges till nothing remains
    while len(currRotten) > 0:
        currRottenCopy = currRotten
        currRotten = [] # we abort if it is still empty after processing the currRottenCopy which means we didn't change anything in this iteration
        for cell in currRottenCopy:
            row = cell[0]
            col = cell[1]
            # check in all directions if there are fresh oranges
            if row - 1 >= 0 and grid[row - 1][col] == 1:
                grid[row - 1][col] = 2 # make it rotten
                currRotten.append([row-1,col]) # add the changed cell to the processing unit
            if row + 1 < rows and grid[row + 1][col] == 1:
                grid[row + 1][col] = 2 
                currRotten.append([row+1 , col]) 
                
            if col - 1 >= 0 and grid[row][col-1] == 1:
                grid[row][col - 1] = 2 
                currRotten.append([row , col-1]) 
                
            if col + 1 < cols and grid[row][col + 1] == 1:
                grid[row][col + 1] = 2 
                currRotten.append([row,col+1]) 
                
        if len(currRotten) > 0:
            numFresh -= len(currRotten)
            result += 1
            
    return result if numFresh == 0 else -1
        
        
        
        

# https://leetcode.com/problems/rotting-oranges/
if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(orangesRotting(grid))
