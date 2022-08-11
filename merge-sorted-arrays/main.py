from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if n == 0:
        # the second array is empty. we don't need to do anything
        return
    
    if m == 0:
        # the first array is empty. copy the second array to the first one
        for i in range(n):
            nums1[i]  = nums2[i]
        return
    
    # swap the zeros with the number in the first array to make sorting easier later
    right = len(nums1) - 1
    left = m - 1
    while left > -1:
        nums1[right] = nums1[left]
        nums1[left] = 0
        left -= 1
        right -= 1


        
    # do normal merge sort
    left1 = len(nums1) - m # left pointer in first array
    left2 = 0 # left pointer in second array
    index = 0 # index to insert elements to at the beginning of the first array
    while left1 < len(nums1) and left2 < n:
        if nums1[left1] <= nums2[left2]:
            nums1[index] = nums1[left1]
            left1 += 1
        else:
            nums1[index] = nums2[left2]
            left2 += 1
        index += 1
            
    while left1 < len(nums1):
        nums1[index] = nums1[left1]
        index += 1
        left1 += 1
        
    while left2 < len(nums2):
        nums1[index] = nums2[left2]
        index += 1
        left2 += 1

        
            
            


if __name__ == "__main__":
    nums1 = [0,1,0,0, 0 , 0]
    m = 1
    nums2 = [2,5,6]
    n = 3
    merge(nums1,m,nums2,n)
    print(nums1)
