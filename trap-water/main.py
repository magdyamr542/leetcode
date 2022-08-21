from typing import List


def trap(height: List[int]) -> int:
    if len(height) <= 2:
        return 0
    
    leftMax = [0 for i in range(len(height))]
    rightMax = [0 for i in range(len(height))]
    
    for i in range(1 , len(height)):
        leftMax[i] = max(height[i-1] , leftMax[i - 1])
        
    for i in range(len(height) - 2 , -1 , -1):
        rightMax[i] = max(height[i + 1] , rightMax[i + 1])
    
    result = 0
    for i in range(len(height)):
        toAdd = min(leftMax[i] , rightMax[i])  - height[i]
        if toAdd > 0:
            result += toAdd
            
    return result

# https://leetcode.com/problems/3sum/
def main():
    height = [0 , 2 , 0 , 3 , 2 , 1 , 3 , 2 , 2 , 4 , 1 , 1 , 2]
    print(trap(height))

if __name__ == "__main__":
    main()
