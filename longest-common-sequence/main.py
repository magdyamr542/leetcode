import numpy
def longest_common_subsequence(w1 , w2):
    if len(w1) == 0 or len(w2) == 0:
        return 0 # no common subsequence

    # init the db array
    dp = [[1000 for j in range(len(w2) + 1)] for i in range(len(w1) + 1)]

    # setup the edges which simulate the empty string
    for i in range(len(w1) + 1):
        dp[i][len(w2)] = 0
    for i in range(len(w2) + 1):
        dp[len(w1)][i] = 0

    for row in range(len(w1) - 1 , -1 , -1):
        for col in range(len(w2) - 1 , -1 , -1):
            # if the current char matches. take it and use the smaller sub problem
            if w1[row] == w2[col]:
                dp[row][col] = 1 + dp[row + 1][col+1]
            else:
                # if not then try to ignore either both of the chars or take one of them
                dp[row][col] =  max(dp[row + 1][col+1] , dp[row][col+1] , dp[row+1][col])

    print(numpy.matrix(dp))
    return dp[0][0]

# https://leetcode.com/problems/longest-common-subsequence/submissions/
def main():
    w1 = "aca"
    w2 = "ca"
    print(f"the longest common subsequence is {longest_common_subsequence(w1,w2)}")

if __name__ == "__main__":
    main()
