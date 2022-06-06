def min_dist(word1 , word2):
    word1_len = len(word1)
    word2_len = len(word2)

    if (word1_len == 0 and word2_len == 0 ):
        return 0
    if (word1_len == 0 and word2_len != 0 ):
        return word2_len # simply add all chars from word2 to word1
    if (word1_len != 0 and word2_len == 0 ):
        return word1_len # simply remove all chars from word2 to word1

    
    dp = [[0 for _ in range(word1_len + 1)] for __ in range(word2_len + 1)]

    # fill the rows and cols for base cases
    for i in range(word2_len + 1):
        dp[i][word1_len] = word2_len - i

    for i in range(word1_len + 1):
        dp[word2_len][i] = word1_len - i

    for row in range(word2_len - 1, -1 , -1 ):
        for col in range(word1_len - 1 , -1 , -1):
            char1 = word1[col]
            char2 = word2[row]
            # if chars are equal then 0 operations are needed
            if char1 == char2:
                dp[row][col] = dp[row + 1][col + 1]
                continue
            # if chars are not equal. try to either (add,remove,replace) and get the minimum
            min_if_removed = dp[row][col + 1]
            min_if_added = dp[row + 1][col]
            min_if_replaced = dp[row + 1][col+1]
            dp[row][col] = 1 + min(min_if_added , min_if_removed , min_if_replaced)

            
    return dp[0][0] # return the min when taking the full two words



# problem https://leetcode.com/problems/edit-distance/
def main():
    word1 = "bc"
    word2 = "abd"
    print(f"this min distance is " , min_dist(word1, word2))

if __name__ == "__main__":
    main()
