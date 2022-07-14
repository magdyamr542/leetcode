def unique_paths(m: int, n: int) -> int:
    dp = [[0 for col in range(n)] for row in range(m)]
    dp[0][0] = 1
    
    for row in range(m):
        for col in range(n):
            if row == 0 or col == 0:
                dp[row][col] = 1
            else:
                dp[row][col] = dp[row - 1][col] + dp[row][col-1] 
             
    return dp[m-1][n-1]
    

# https://leetcode.com/problems/unique-paths
def main():
    m = 3
    n = 2
    result = unique_paths(m,n)
    print(f"unique paths for m={m} and n={n} is {result}")

if __name__ == "__main__":
    main()
