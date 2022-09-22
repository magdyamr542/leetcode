
from typing import List

def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False
    
    count = {}
    for num in hand:
        if count.get(num):
            count[num] += 1
        else:
            count[num] = 1
            
    hand.sort()
    groups = 0
    for curr in hand:
        if count.get(curr) == 0:
            continue
        count[curr] -= 1
        for adder in range(1,groupSize):
            if not count.get(curr + adder):
                return False
            count[curr + adder] -= 1
        groups += 1
            
    return groups == len(hand) // groupSize
    
    

# https://leetcode.com/problems/hand-of-straights
def main():
    hand = [1,2,3,6,2,3,4,7,8]
    group = 3
    print(isNStraightHand(hand , group))

if __name__ == "__main__":
    main()
