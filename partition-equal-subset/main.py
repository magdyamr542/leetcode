from typing import List


def canPartition( nums: List[int]) -> bool:
    total = 0
    for num in nums:
        total += num
        
    # if the total is odd. we cannot partition to two halfs
    if total % 2 == 1:
        return False
    
    # check if there is a subarray which sums to half
    # if that is the case. there is another sub arrray with the same half and we return true
    half = total // 2
    # dp[row][col] is True if we there are nums with indexes 0..row where the sum of these nums can be equal to col
    # dp[3][10] is True if we have nums that sum up to 10 while using nums with indexes 0,1,2,3 
    dp = [[False for col in range(half)]for row in range(len(nums))]
    
    for row in range(len(nums)):
        for col in range(half):
            num = nums[row]
            target = col + 1
            if num == target:
                dp[row][col] = True
                continue
                
            # if we can make the target ignoring the current num
            if row > 0 and dp[row-1][col] == True:
                dp[row][col] = True
                continue
            
            remaining_target = target - num
            remaining_target_col = remaining_target - 1
            if row > 0 and remaining_target_col >= 0 and dp[row-1][                remaining_target_col] == True:
                dp[row][col] = True
                    
    return dp[len(nums)-1][half-1]
                      
                    
                        
                        
        



# https://leetcode.com/problems/partition-equal-subset-sum/
def main():
    nums = [1,2,3,5]
    print(canPartition(nums))

if __name__ == "__main__":
    main()
