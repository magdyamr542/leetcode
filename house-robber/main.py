from typing import List
import time

# using dp. better time complexity. linear
def houseRobberDp(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    
    if len(nums) == 2:
        return max(nums)
    
    # for each num we can either take it or leave it
    # if we took it. we can't take the number before it.
    # if we left it. we just get the max from the number before it or between it.
    dp = [nums[0] , max(nums[0] , nums[1])]
    for i in range(2,len(nums)):
        # when taking it
        taking = nums[i] + dp[i-2]
        leaving = dp[i-1] 
        dp.append(max(taking , leaving))
        
    return max(dp[-1] , dp[-2])
    
    

# using a decision tree. bad time complexity
def houseRobber(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums)

    def backtrack(currIndex , currResult) -> int:
        # base cases
        if currIndex >= len(nums):
            return currResult
        # take the currrent number and then go to other valid indexes
        return max(backtrack(currIndex + 2 , currResult + nums[currIndex] ), backtrack(currIndex + 3 , currResult + nums[currIndex]))
    
    return max(backtrack(0 , 0) , backtrack(1 , 0))

# https://leetcode.com/problems/house-robber/
def main():
    nums = [2,7,9,3,1,3,1,5,7,78,3,45,234,2,4,2,3,5,6,2,3,4,3,5,2,3,41,234,2,2,3,2,3,2,2,3,32,111,1,1,1,1,2,31,,22,3,4,234,32,43,4,3144]
    startDT = time.time()
    print("DT solution=",houseRobber(nums))
    endDT = time.time()
    print("time for DT approach" , endDT - startDT)

    startDP = time.time()
    print("DP solution=",houseRobberDp(nums))
    endDP = time.time()
    print("time for DP approach" , endDP - startDP)



    print(houseRobberDp(nums))

if __name__ == "__main__":
    main()
