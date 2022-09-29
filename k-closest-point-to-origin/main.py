from typing import List
import heapq


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    result = [] # will hold the k closet points to the origin
    minHeap = [] # a min heap of size k. the elements are tuples (dist to origin,x,y)
    for point in points:
        dist = point[0] ** 2 + point[1] ** 2
        heapq.heappush(minHeap , [-dist , point])
        if len(minHeap) > k:
            heapq.heappop(minHeap)
    return list(map(lambda item: item[1] , minHeap))
    
    
    
# https://leetcode.com/problems/k-closest-points-to-origin/
def main():
    points = [[3,3],[5,-1],[-2,4]]
    k =2 
    print(kClosest(points ,k))

if __name__ == "__main__":
    main()
