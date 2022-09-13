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
            

def networkDelayTimeBfs( times: List[List[int]], n: int, k: int) -> int:
    # bfs to calculate the delay times
    # if a node is not reachable return -1
    edges_map = {}
    for time in times:
        src,dst,cost = time
        if edges_map.get(src):
            edges_map[src].append([dst,cost])
        else:
            edges_map[src] = [[dst,cost]]
            
    # the distances from the node k to all other nodes
    # if the distance after the bfs is still inf. the node is not reachable by k
    distances = [float("inf")] * (n + 1)
    distances[k] = 0
    
    # a queue that has all nodes to be processed
    queue = [(0 , k)] 
    while queue:
        currCost , currNode  =  queue.pop(0)
        if distances[currNode] < currCost:
            continue
        for neighbor in edges_map.get(currNode , []):
            neighborNode , neighborCost = neighbor
            if neighborCost + currCost < distances[neighborNode]:
                distances[neighborNode] = currCost + neighborCost
                queue.append((currCost + neighborCost , neighborNode ))
            
    maxResult = max(distances[1:])
    return int(maxResult) if maxResult != float("inf") else -1
    
    



# https://leetcode.com/problems/network-delay-time/submissions/
def main():
    times = [[1,2,1]]
    n = 2
    k = 2
    print("with dijkstra" , networkDelayTime(times,n,k))
    print("with bfs" , networkDelayTimeBfs(times,n,k))

if __name__ == "__main__":
    main()
