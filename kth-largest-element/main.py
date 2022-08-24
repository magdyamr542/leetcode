from typing import List
import heapq


def findKthLargest(nums : List[int] , k : int) -> int:
    heapq._heapify_max(nums)
    for _ in range(k -1):
         heapq._heappop_max(nums)
    return nums[0]

def findKthLargestQuickSelect(nums : List[int] , k : int) -> int:
    def partition(left , right , pivotIndex) -> int:
        pivotValue = nums[pivotIndex]
        # swap the pivot value with the num at the right
        nums[right] , nums[pivotIndex] = nums[pivotIndex] , nums[right]
        swapIndex = left
        for i in range(left , right):
            if nums[i] < pivotValue:
                nums[swapIndex] , nums[i] = nums[i] , nums[swapIndex]
                swapIndex += 1

        nums[swapIndex] , nums[right] = nums[right] , nums[swapIndex]
        return swapIndex

        
    def find(left , right):
        n = len(nums) 
        pivotIndex = (left + right) // 2
        pivotIndexAfterPartition = partition(left , right , pivotIndex)
        if k == n - pivotIndexAfterPartition:
            return nums[pivotIndexAfterPartition]
        elif k > n - pivotIndexAfterPartition:
            return find(left , pivotIndexAfterPartition - 1)
        else:
            return find(pivotIndexAfterPartition + 1 , right)

            

    return find(0 , len(nums) - 1)


    
        

# https://leetcode.com/problems/kth-largest-element-in-an-array/
if __name__ == "__main__":
    nums=  [6,2,3,5,1,4]
    k = 2
    print("heap", findKthLargest(nums.copy() , k))
    print("quicksearch" , findKthLargestQuickSelect(nums.copy() , k))
