def isMatch(s: str, p: str) -> bool:
    m = {} # maps an index of a row to the first true value in the dp array
    dp = [[False for j in range(len(s) + 1)]for i in range(len(p) + 1)]
    dp[-1][-1] = True
    m[len(p)] = len(s)
    # add values for the last col
    for i in range(len(p) - 1 , -1 , -1):
        if p[i] == "*" and dp[i+1][-1] == True:
            m[i] = len(s)
            dp[i][-1] = True
        
    for i in range(len(p) - 1, -1 ,-1):
        for j in range(len(s) - 1, -1 , -1):
            if (p[i] == s[j] or p[i] == "?") and dp[i+1][j+1]:
                if m.get(i , -1) == -1:
                    m[i] = j
                dp[i][j] = True
            elif p[i] == "*":
                if m.get(i+1 , -1) != -1 and m.get(i+1) >= j: 
                    if m.get(i , -1) == -1:
                        m[i] = j
                    dp[i][j] = True
                
    return dp[0][0]
        
            
                
# https://leetcode.com/problems/wildcard-matching/submissions/
if __name__ == "__main__":
    print(isMatch("ab" , ".*"))


    
