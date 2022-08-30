from typing import List 
import math

def minEatingSpeed(piles: List[int], h: int) -> int:
    if len(piles) == 1:
        if piles[0] < h:
            return 1
        return math.ceil(piles[0] / h)
    
    def getTotal(mid):
        result = 0
        for i in range(len(piles)):
            result += math.ceil(piles[i] / (mid + 1))
        return result
    
    # try to make the speed less if we can
    piles.sort()
    result = piles[len(piles) - 1] # biggest speed as default
    left = 0
    right = result
    while left <= right:
        mid = (left + right) // 2
        totalWhenUsingMid = getTotal(mid)
        if totalWhenUsingMid > h:
            left = mid + 1
        elif totalWhenUsingMid <= h:
            result = min(result ,mid + 1)
            # can we make it with less speed ?
            right = mid - 1
            
    return result
        
        
    
    
    
                
                
# https://leetcode.com/problems/koko-eating-bananas/
if __name__ == "__main__":
    piles = [3,6,7,11]
    h = 8
    print(minEatingSpeed(piles , h))


    
