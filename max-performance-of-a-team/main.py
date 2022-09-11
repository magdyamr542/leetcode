from typing import List
import heapq


def maxPerformance( n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    # greedy algorithm that does the following
    # starting from a certain efficiency. can we add to it another engineer with high speed to make the overall better
    speedAndEff = []
    for i in range(len(speed)):
        speedAndEff.append([speed[i] , efficiency[i]])

    # the result
    result = 0
    # sort by the efficiency
    speedAndEff.sort(key=lambda pair: pair[1] , reverse=True)
    # a min heap of size k - 1 that will hold the speeds
    minHeap = []
    currHeapSum = 0
    for i in range(len(speed)):
        currSpeed , currEff = speedAndEff[i]
        result = max(result , currEff *( currHeapSum + currSpeed))
        heapq.heappush(minHeap , currSpeed)
        currHeapSum += currSpeed
        if len(minHeap) == k:
            currHeapSum -= minHeap[0]
            heapq.heappop(minHeap)
    return result % (pow(10,9) + 7)

        
# https://leetcode.com/problems/maximum-performance-of-a-team/
def main():
    n= 6
    k=2
    speed = [2,10,3,1,5,8] 
    efficiency = [5,4,3,9,7,2]
    print(maxPerformance(n,speed, efficiency , k))

if __name__ == "__main__":
    main()
