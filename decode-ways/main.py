def numDecodings(s: str) -> int:
    if len(s) == 0:
        return 0
    
    if len(s) == 1:
        return 0 if s[0] == '0' else 1

    dp = [0 for i in range(len(s))]

    for i in range(len(dp) - 1 , -1 , -1):
        if s[i] == '0':
            dp[i] = 0
            continue
        if i == len(dp) - 1:
            dp[i] = 1 if s[i] != '0' else 0
        else:
            if dp[i+1] != 0:
                dp[i] += dp[i+1] # taking one char
            if int(s[i] + s[i+1]) <= 26:
                if i+2 < len(s):
                    dp[i] += dp[i+2] # taking two chars
                else:
                    dp[i] += 1

    return dp[0]
        
    

# https://leetcode.com/problems/decode-ways/
if __name__ == "__main__":
    print(numDecodings("11106"))


    
