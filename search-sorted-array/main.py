from typing import List


def search(nums: List[int], target: int) -> int:
    if len(nums) == 1:
        return -1 if nums[0] != target else 0

    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        numMid = nums[middle]
        
        if numMid == target:
            return middle
        
        if nums[left] < nums[right]:
            # perfectly sorted. use normal bin search
            if numMid > target:
                right = middle - 1
            else:
                left = middle + 1
            continue
                
        
        if numMid > target:
            numMidPartBigArr = numMid > nums[-1]
            targetPartBigArr = target > nums[-1]
            if numMidPartBigArr and targetPartBigArr:
                right = middle - 1
            elif numMidPartBigArr and not targetPartBigArr:
                left = middle + 1
            elif not numMidPartBigArr and not targetPartBigArr:
                right = middle -1
            else:
                break
        else:
            numMidPartBigArr = numMid > nums[-1]
            targetPartBigArr = target > nums[-1]
            if numMidPartBigArr and targetPartBigArr:
                left = middle + 1
            elif not numMidPartBigArr and not targetPartBigArr:
                left = middle + 1
            elif not numMidPartBigArr and targetPartBigArr:
                right = middle - 1
            else:
                break
            
    return -1
            
    
    


# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
def main():
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(search(nums , target))

if __name__ == "__main__":
    main()
