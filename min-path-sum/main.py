from typing import List


def minPathSum( grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for col in range(cols)] for row in range(rows)]
        dp[0][0] = grid[0][0]
        
        # fill the first row
        for col in range(1, cols):
            dp[0][col] = grid[0][col] + dp[0][col-1]
            
        # fill the first col
        for row in range(1, rows):
            dp[row][0] = grid[row][0] + dp[row-1][0]
            
        # first the rest of the dp array 
        for row in range(1 , rows):
            for col in range(1, cols):
                dp[row][col] = grid[row][col] + min(dp[row-1][col] , dp[row][col-1])
        return dp[rows-1][cols-1]
        
        
        

def genAllPaths( grid: List[List[int]]) -> List[int]:
    for i in grid:
        print('\t'.join(map(str, i)))

    result = []
    def dfs(row : int , col : int , curr_path : List[int]):
        # base cases
        # 1. out of bounds
        if row >= len(grid) or col >= len(grid):
            return


        curr_path.append(grid[row][col])

        # 2. reached destination
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            result.append(curr_path)
            return

        # go down
        dfs(row + 1 , col , curr_path.copy())
        # go right
        dfs(row , col + 1 , curr_path.copy())

    dfs(0 , 0 , [])
    return result


# https://leetcode.com/problems/minimum-path-sum/
def main():
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(minPathSum(grid))
    print(genAllPaths(grid))

if __name__ == "__main__":
    main()
