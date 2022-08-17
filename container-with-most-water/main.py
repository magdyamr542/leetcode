from typing import List 

def maxArea(height: List[int]) -> int:
    if len(height) == 2:
        return min(height[0] , height[1])
        
    result = - 1
    left =  0
    right = len(height) - 1
    while left < right:
        currArea = (right - left) * min(height[left] , height[right])
        if currArea > result:
            result = currArea
        
        # try to optimize the pointer for the smallest value
        if height[left]  <= height[right]:
            currLeft = height[left] 
            left += 1
            while left < right and height[left] <= currLeft:
                left += 1
        else:
            currRight = height[right] 
            right -= 1
            # try to optimize the pointer for the smallest value
            while left < right and height[right] <= currRight:
                right -= 1
    
    return result
            
                
#https://leetcode.com/problems/binary-tree-level-order-traversal/
if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))


    
