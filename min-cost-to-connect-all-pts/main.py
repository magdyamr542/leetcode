from typing import List
import heapq

def minCostToConnectAllPoints( points: List[List[int]]) -> int:
    # create adjacency list of edges map
    edges = {i : [] for i in range(len(points))}
    for i in range(len(points)):
        x1 , y1 = points[i]
        for j in range(i+1 , len(points)):
            x2,y2 = points[j]
            dist = abs(x1-x2) + abs(y1-y2)
            edges[i].append([j,dist])
            edges[j].append([i,dist])
    result = 0
    queue = [[0,0]] # array of (cost , node index)
    visited = set() # the nodes indexes in the min spanning tree
    while len(visited) != len(points):
        # get the node with the minimum
        cost , nodeIndex = heapq.heappop(queue)
        if nodeIndex in visited:
            continue
        visited.add(nodeIndex)
        result += cost
        for neighbor in edges.get(nodeIndex , []):
            neighborIndex , neighborCost = neighbor
            if neighborIndex not in visited:
                heapq.heappush(queue , [neighborCost , neighborIndex])

    return result

# https://leetcode.com/problems/min-cost-to-connect-all-points/
def main():
    points = [[3,12],[-2,5],[-4,1]]
    print(minCostToConnectAllPoints(points))

if __name__ == "__main__":
    main()
