from typing import List 
import math

def minEatingSpeed( piles: List[int], h: int) -> int:
    # maxSpeed to eat with is max(piles). With this speed we finish in len(piles) hours
    # minSpeed to eat with is min(piles). 
    # desired speed would be between those two. minSpeed <= speed <= maxSpeed
    # create an array with possibles speeds. [minSpeed , minSpeed+1 , .... , maxSpeed]
    # do a binary search in this array for the desired speed.
    # assume we found a speed si with which we can finish under h hours. this means that there is a  
    # possbility to find another speed sj < si to finish under h hours. so decrease the search space of the binary search
    # assume we found a speed si with which we can finish in more than h hours. this means that there is a  speed sj > si to finish withing h hours. so decrease the search space of binary search
    def get_num_hours_to_finish(speed : int) -> int:
        # return the number of hours required to finish eating the piles
        # using the given eating speed 
        result = 0
        for pile in piles:
            if pile <= speed:
                result += 1 # we wait after finishing
            else:
                result += math.ceil(pile / speed) # we finish the pile in multiple rounds
        return result
    
    # example [3,6,7,11], h = 8
    # minSpeed=3, maxSpeed=11, resultSpeed=11, speeds = [3,4,5,6,7,8,9,10,11]
    # 1. left=0, right=7, middle=3, curr_speed=6, hours_using_curr_speed=6, resultSpeed=11
    # 2. left=0, right=2, middle=1, curr_speed=4, hours_using_curr_speed=8, resultSpeed=6
    # 3. left=0, right=1, middle=0, curr_speed=3, hours_using_curr_speed=10, resultSpeed=4
    # 4. left=1, right=1, break
    # return resultSpeed=4

    left = 1 # min speed
    right = max(piles) # max speed
    resultSpeed = right  # initially, assume worst case. we need to use the biggest speed in order to finish
    while left < right:
        middle = (left + right) // 2
        curr_speed = middle
        hours_using_curr_speed = get_num_hours_to_finish(curr_speed)
        if hours_using_curr_speed <= h:
            # we can find a smaller speed to eat and still finish
            resultSpeed = min(resultSpeed , curr_speed)
            right = middle - 1
        else:
            # we need to have a bigger speed
            left = middle + 1
    
    return resultSpeed
            
        
# https://leetcode.com/problems/koko-eating-bananas/
if __name__ == "__main__":
    piles = [3,6,7,11]
    h = 8
    print(minEatingSpeed(piles , h))


    
