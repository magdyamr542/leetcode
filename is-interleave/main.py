def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    dp = [ [False for col in range(len(s2) + 1)] for row in range(len(s1) + 1)]
    dp[len(s1)][len(s2)] = True # empty strings
    
    for row in range(len(s1) , -1 , -1):
        for col in range(len(s2) , -1 , -1):
            if row < len(s1) and s3[row + col] == s1[row] and dp[row+1][col]:
                dp[row][col] = True
            if col < len(s2) and s3[row + col] == s2[col] and dp[row][col+1]:
                dp[row][col] = True
    return dp[0][0] == True
    

            
                
# https://leetcode.com/problems/interleaving-string/submissions/
if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(isInterleave(s1,s2,s3))


    
