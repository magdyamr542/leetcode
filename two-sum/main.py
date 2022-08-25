from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        numl = numbers[left]
        numr = numbers[right]
        if numl + numr == target:
            return [left + 1 , right + 1]
        elif numl + numr < target:
            left += 1
            
        else:
            right -= 1
            
    return [0,0]
    
    

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 3
    print(twoSum(nums , target))
