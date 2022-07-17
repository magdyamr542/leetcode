from typing import List

def getAncestors(n: int, edges: List[List[int]]) -> List[List[int]]:
    # maps a node to a list of the edges that goes to it 
    edges_map = dict.fromkeys(range(n) , [])
    for edge in edges:
        src = edge[0]
        dst = edge[1]
        if edges_map.get(dst , None):
            edges_map[dst].append(src)
        else:
            edges_map[dst] = [src]
       
    def dfs(src , result , visited):
        if len(edges_map[src]) == 0:
            return 
        
        for dst in edges_map[src]:
            if dst in visited:
                continue
            result.append(dst)
            visited.add(dst)
            dfs(dst , result , visited)
            
    result = []
    for node in range(n):
        reachable = []
        dfs(node , reachable , set())
        reachable.sort()
        result.append(reachable)
    return result
            
        
        
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/submissions/
if __name__ == "__main__":
    n = 8
    edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
    print(getAncestors(n , edgeList))
    
