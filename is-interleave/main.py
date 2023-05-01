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



def isInterleaveDp(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    # dp[i][j] answers the question if there is a string interleaving 
    # using chars s1[i:] and s2[j:] to generate s3[i+j:]

    # dp[0][0] means, is there string interleaving using all of s1 and s2
    # to generate all of s3

    # when having empty spaces, it's a base case
    rows = len(s1) + 1
    cols = len(s2) + 1
    dp = [[False for _ in range(cols)] for _ in range(rows)]
    dp[-1][-1] = True # two empty strings from s1, s2 can generate an empty string in s3

    for row in range(rows - 2 , -1 , -1):
        if s3[row + cols - 1] == s1[row]:
            dp[row][cols - 1] = dp[row + 1][cols-1]

    for col in range(cols - 2 , -1 , -1):
        if s3[rows-1 + col] == s2[col]:
            dp[rows-1][col] = dp[rows - 1][col + 1]

    for row in range(rows-2 , -1 , -1):
        for col in range(cols-2, -1 , -1):
            # either pick char from s1 or s2
            if s1[row] == s3[row + col] and dp[row + 1][col]:
                dp[row][col] = True
            if s2[col] == s3[row + col] and dp[row][col+1]:
                dp[row][col] = True


    return dp[0][0]


def isInterleaveRecursive(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    # dfs(i,j) returns true, if there is an interleaving starting from s1[i] s2[j] for the string s
    def dfs(i , j) -> bool:
        # base case
        if i == len(s1) and j == len(s2):
            return True # found an interlaving
        # choose either a character from s1 or from s2
        choose_s1 , choose_s2 = False , False
        if i < len(s1) and s1[i] == s3[i+j]:
            choose_s1 = dfs(i + 1 , j)

        if j < len(s2) and s2[j] == s3[i+j]:
            choose_s2 = dfs(i , j + 1)

        return choose_s1 or choose_s2


    return dfs(0 , 0)

            
                
# https://leetcode.com/problems/interleaving-string/submissions/
if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(isInterleave(s1,s2,s3))
    print(isInterleaveRecursive(s1,s2,s3))
    print(isInterleaveDp(s1,s2,s3))


    
