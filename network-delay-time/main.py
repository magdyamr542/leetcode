from typing import List
import heapq

def networkDelayTime( times: List[List[int]], n: int, k: int) -> int:
    # dijkstra algorithm. get the shortest path from k to all other nodes
    # if a node is not reachable return -1
    edges_map = {}
    for time in times:
        src,dst,cost = time
        if edges_map.get(src):
            edges_map[src].append([dst,cost])
        else:
            edges_map[src] = [[dst,cost]]
            
    # the visited nodes
    visited = set()
    
    # heap of tuples (min path between k and currNode , currNode)
    # at the beginning k can reach itself with 0 dist
    heap = [(0 , k)] 
    result = 0
    
    while heap:
        currCost , currNode  =  heapq.heappop(heap)
        if currNode in visited:
            continue
            
        visited.add(currNode)
        result = max(result , currCost)
        for neighbor in edges_map.get(currNode , []):
            neighborNode , neighborCost = neighbor
            if neighborNode in visited:
                continue
            heapq.heappush(heap , (neighborCost + currCost , neighborNode))
            
    return result if len(visited) == n else -1
            
    
    



# https://leetcode.com/problems/network-delay-time/submissions/
def main():
    pass

if __name__ == "__main__":
    main()
