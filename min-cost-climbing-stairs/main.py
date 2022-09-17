from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    minToReachFirst = 0
    minToReachSecond = 0
    for i in range(2,len(cost)):
        minToReachCurr = min(minToReachFirst + cost[i-2] , minToReachSecond + cost[i-1])
        minToReachFirst = minToReachSecond
        minToReachSecond = minToReachCurr
    return min(minToReachFirst + cost[-2] , minToReachSecond + cost[-1])
        
    


# https://leetcode.com/problems/min-cost-climbing-stairs/submissions/
def main():
    cost = [10,15,20]
    print(minCostClimbingStairs(cost))

if __name__ == "__main__":
    main()
