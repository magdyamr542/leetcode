def get_min_num_coins(coins , count):
    # init the db array. an entry at index i answers the question
    # what is the min number of coins needed to generate a count equal to i
    dp = [count + 1 for i in range(count + 1)]
    for current_count in range(len(dp)):
        if current_count == 0:
            dp[current_count] = 0 # to generate count of 0. we don't use any coins
        else:
            for coin in coins:
                if current_count - coin >= 0:
                    # it means we can use this coin to generate a count 
                    dp[current_count] =  min(dp[current_count] , 1 + dp[current_count - coin])

    print(dp)
    return dp[count] if dp[count] < (count + 1) else -1


def main():
    coins = [4,1,4,3]
    result = 10
    print(f"the min number of coins to generate the sum is {get_min_num_coins(coins , result)}")

if __name__ == "__main__":
    main()
