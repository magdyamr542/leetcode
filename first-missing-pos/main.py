from typing import List

def firstMissingPositive(nums: List[int]) -> int:
    
    max_marker = len(nums) + 2 # can never be in the output space. use it to replace 0 values
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0
            
    for i in range(len(nums)):
        curr_num = abs(nums[i])
        if curr_num >= 1 and curr_num <= len(nums):
            index_in_sorted_arr = curr_num - 1
            if nums[index_in_sorted_arr] > 0:
                    nums[index_in_sorted_arr] = -1 *  nums[index_in_sorted_arr]
            elif nums[index_in_sorted_arr] == 0:
                nums[index_in_sorted_arr] = -1 * max_marker
            
            
    for i in range(1 , len(nums) + 1):
        index_in_sorted_arr = i - 1
        if nums[index_in_sorted_arr] >= 0:
            return i
            
    return len(nums) + 1
            
        
        

# https://leetcode.com/problems/first-missing-positive/
def main():
    nums = [7,8,9,11,12]
    print(firstMissingPositive(nums))

if __name__ == "__main__":
    main()
