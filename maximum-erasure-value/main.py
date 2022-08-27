from typing import List


def maximumUniqueSubarray( nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    
    if len(nums) == 1:
        return nums[0]
    
    numset = set()
    left = 0
    right = 0
    result = 0
    maxResult = 0
    while right < len(nums) and left < len(nums):
        currnum = nums[right]
        while left <= right and currnum in numset:
            # make the window smaller
            numset.remove(nums[left])
            result -= nums[left]
            left += 1
        numset.add(currnum)
        result += currnum
        maxResult = max(result , maxResult) 
        right += 1
    return maxResult
        
    
     
        
# https://leetcode.com/problems/maximum-erasure-value/
if __name__ == "__main__":
    nums = [4,2,4,5,6]
    print(maximumUniqueSubarray(nums))
