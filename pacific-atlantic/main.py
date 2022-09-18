
from typing import List

def print2D(grid):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in grid]))
    print()

def pacificAtlantic( grid: List[List[int]]) -> List[List[int]]:

    # grid where grid[r][c] = True if the cell at r,c can reach the pacific
    rows = len(grid)
    cols = len(grid[0])
    
    # 1 means it can reach the pacific
    # -1 means it can't reach the pacific
    # 0 means we didn't check yet
    pac = [ [0 for col in range(cols)] for row in range(rows)]
    atlantic = [ [0 for col in range(cols)] for row in range(rows)]
    beingVisited = [ [False for col in range(cols)] for row in range(rows)]

    # all cells at the top or left can reach the pac
    for row in range(rows):
        pac[row][0] = 1
    for col in range(cols):
        pac[0][col] = 1

    # all cells at the bottom or right can reach the atlantic
    for row in range(rows):
        atlantic[row][cols-1] = 1
    for col in range(cols):
        atlantic[rows-1][col] = 1
        
    def canGo(fromR,fromC,toR,toC):
        return toR >= 0 and toR < rows and toC >= 0 and toC < cols and grid[fromR][fromC] >= grid[toR][toC] and not beingVisited[toR][toC]
    
    # return true if the one can reach the pacific from row,col
    def dfs(row,col,isPacific):

        # reached a cell that can reach the pacific
        if isPacific and pac[row][col] == 1:
            return 1
        
        # reached a cell that can't reach the pacific
        if isPacific and pac[row][col] == -1:
            return -1

        if not isPacific and atlantic[row][col] == 1:
            return 1
        
        # reached a cell that can't reach the pacific
        if not isPacific and atlantic[row][col] == -1:
            return -1
        
        beingVisited[row][col] = True

        # left
        if canGo(row,col,row,col-1) and dfs(row,col-1,isPacific) == 1:
            beingVisited[row][col] = False
            return 1
        # right
        if canGo(row,col,row,col+1) and dfs(row,col+1,isPacific) == 1:
            beingVisited[row][col] = False
            return 1
        # up
        if canGo(row,col,row-1,col) and dfs(row-1,col,isPacific) == 1:
            beingVisited[row][col] = False
            return 1
        # down
        if canGo(row,col,row+1,col) and dfs(row+1,col,isPacific) == 1:
            beingVisited[row][col] = False
            return 1
        
        beingVisited[row][col] = False
        # could not reach the pacific 
        return -1
        
    # check for the rest of the cells if they can reach the pac
    for row in range(1 , rows):
        for col in range(1 , cols):
            if pac[row][col] == 0:
                pac[row][col] = dfs(row,col,True) # we didn't check this cell yet

    for row in range(0 , rows-1):
        for col in range(0 , cols-1):
            if atlantic[row][col] == 0:
                atlantic[row][col] = dfs(row,col,False) # we didn't check this cell yet


    # merge the two results
    result = []
    for row in range(rows):
        for col in range(cols):
            if pac[row][col] == 1 and atlantic[row][col] == 1:
                result.append([row,col])

    
    return result
    
# https://leetcode.com/problems/pacific-atlantic-water-flow/
def main():
    grid = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(pacificAtlantic(grid))

if __name__ == "__main__":
    main()
