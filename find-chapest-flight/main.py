from typing import List
import math


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # map for the edges. maps a src to [dst,cost]
    edges = {}
    for flight in flights:
        if edges.get(flight[0]):
            edges[flight[0]].append([flight[1] , flight[2]])
        else:
            edges[flight[0]] = [[flight[1] , flight[2]]]
    result = 0             
    
    queue = [[src,0,k]] # array of [node,currentCost,k left , coming from] # if k left = 0 it means we cannot use a node in the middle
    costSeen = [math.inf] * n
    while len(queue) != 0:
        current = queue.pop(0)
        currNode , currCost , currK = current
        # reached the dist
        if currNode == dst:
            result = min(result , currCost) if result != 0 else currCost
            continue
        costSeen[currNode] = min(costSeen[currNode] , currCost)

        # get neighbor nodes
        neighborNodes = edges.get(currNode , [])
        for nNode in neighborNodes:
            node = nNode[0]
            cost = nNode[1]
            if node == dst:
                queue.append([node , currCost + cost , currK])
            elif currK > 0 and costSeen[node] > currCost + cost:
                queue.append([node , currCost + cost , currK - 1])
            
        
    return result if result > 0 else -1
            
    


# https://leetcode.com/problems/cheapest-flights-within-k-stops
def main():
    n = 5
    flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
    src = 0
    dst=2
    k = 2
    print(findCheapestPrice(n,flights , src,dst,k))

if __name__ == "__main__":
    main()
