from typing import List


def islandPerimeter(grid: List[List[int]]) -> int:
    result = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                continue
             # top
            if row == 0 or grid[row-1][col] == 0:
                result += 1
                
             # bottom
            if row == len(grid) - 1 or grid[row + 1][col] == 0:
                result += 1
                
             # left
            if col == 0 or grid[row][col-1] == 0:
                result += 1
                
             # right
            if col == len(grid[0]) - 1 or grid[row][col+1] == 0:
                result += 1
                
            
    return result                  
    
    


# https://leetcode.com/problems/island-perimeter/
def main():
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(islandPerimeter(grid))

if __name__ == "__main__":
    main()
