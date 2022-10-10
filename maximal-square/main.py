from typing import List


def maximalSquare(matrix: List[List[str]]) -> int:
        rows , cols = len(matrix) , len(matrix[0])
        dp = [[ int(matrix[row][col]) for col in range(cols)]for row in range(rows)]
        for row in range(rows - 2 , -1 , -1):
            for col in range(cols - 2 , -1 , -1):
                curr = matrix[row][col]
                if curr == "0":
                    dp[row][col]  = 0
                else:
                    dpRight = dp[row][col+1]
                    dpDown = dp[row+1][col]
                    dpRightDown = dp[row+1][col+1]
                    if dpRight == 0 or dpDown == 0 or dpRight == 0:
                        dp[row][col] = 1
                    else:
                        dp[row][col] = 1 + min(dpRight,dpDown,dpRightDown)
                        
        result = 0                
        for row in range(rows):
            for col in range(cols):
                result = max(result , dp[row][col])
        return result * result
    

            
                
# https://leetcode.com/problems/maximal-square/
if __name__ == "__main__":
     matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
     print(maximalSquare(matrix))


    
