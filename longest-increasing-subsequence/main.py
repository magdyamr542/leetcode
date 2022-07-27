from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    # dp[i] is the longest increasing subsequence from the start of the array till the index i
    # at the begining every number is a subsequence of length 1
    dp = [1 for i in range(len(nums))]
    
    # the first in dp will always have 1 as value
    for i in range(1 , len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i] , 1 + dp[j])
                
    return max(dp , default=0)
    

# https://leetcode.com/problems/longest-increasing-subsequence/
def main():
    nums = [10,9,2,5,3,7,101,18]
    print(lengthOfLIS(nums))

if __name__ == "__main__":
    main()
