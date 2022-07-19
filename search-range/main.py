from typing import List

def searchRange( nums: List[int], target: int) -> List[int]:
    if len(nums) == 0:
        return [-1,-1]
    left = 0 
    right = len(nums)  - 1
    left_index = -1
    right_index = -1
    
    # get the left most index
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            left_index = mid
            # found the number get the left bounadry
            if mid - 1 > -1 and nums[mid - 1] == nums[mid]:
                right = mid - 1
            else:
                break
                
    left = 0
    right = len(nums) - 1
    # get the right most index
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right_index = mid
            # found the number. get the right boundary
            if mid + 1 < len(nums)  and nums[mid + 1] == nums[mid]:
                left = mid + 1
            else:
                break
                
            
            
    return [left_index , right_index]
        
    
#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
if __name__ == "__main__":
    nums = [5,7,7,8,8,10] 
    target = 8
    print(searchRange(nums , target))
