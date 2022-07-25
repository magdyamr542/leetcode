def maxProfit(prices):
    if len(prices) <=1:
        return 0
    right = len(prices) - 1 
    left = right - 1
    max_profit = 0
    while left > -1:
        if prices[left] > prices[right]:
            right = left
            left -= 1
            continue
        curr_prof = prices[right] - prices[left]
        if curr_prof > max_profit:
            max_profit = curr_prof
        left -= 1
            
    return max_profit
            
            
            
        

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
def main():
    prices = [1,6,4,3,1]
    print(maxProfit(prices))

if __name__ == "__main__":
    main()
