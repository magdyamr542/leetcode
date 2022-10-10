from typing import List


def longestIncreasingPath(matrix: List[List[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    result = 0
    cache = {}
    def dfs(row,col,visited , res):
        if (row,  col) in cache:
            print(f"row={row},col={col}, res={res} , visited={visited}")
            print(cache)
            print("return " , cache.get((row,col)) + res - 1)
            print()
            return cache.get((row,col)) + res - 1

        # out of bounds
        if (row,col) in visited:
            return res 
        
        curr = matrix[row][col]
        currRes = res
        if row + 1 < rows and matrix[row+1][col] > curr:
            res = max(res , dfs(row+1,col,visited + [(row , col)] , currRes + 1))
            
        if row - 1 > -1 and matrix[row-1][col] > curr:
            res = max(res , dfs(row-1,col,visited + [(row , col)] , currRes + 1))
            
        if col + 1 < cols and matrix[row][col+1] > curr:
            res = max(res , dfs(row,col+1,visited + [(row , col)] , currRes + 1))
            
        if col - 1 > -1  and matrix[row][col-1] > curr:
            res = max(res , dfs(row,col-1,visited + [(row , col)] , currRes + 1))
         
        cache[(row,col)] = res - len(visited)
        return res
        
    for row in range(rows):
        for col in range(cols):
            result = max(result,dfs(row,col,[] , 1))

    return result
    

            
                
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
if __name__ == "__main__":
    #matrix = [[3,4,5],[3,2,6],[2,2,1]]
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    print(longestIncreasingPath(matrix))


    
