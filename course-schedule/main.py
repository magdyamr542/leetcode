from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # first build a graph from the prerequisites
    # then check if the graph has a cycle (if yes. return false because there is a deadlock)
    # (if no. return true)
    # checking if the graph has a cycle 
    nodes = range(numCourses)
    edges = {} # maps a node n to a list of nodes m where n->m is an edge in the graph
    
    # build the graph
    for edge in prerequisites:
        src = edge[0] 
        dst = edge[1] 
        if edges.get(src , None):
            edges[src].append(dst)
        else:
            edges[src] = [dst]
    
    # check if the graph has a cycle by doing a simple dfs
    # if during the dfs the rootNode was visited again then there is a cycle
    def hasCycle(node , visited , verified):
        if visited[node]:
            return True # we are visiting a node which has been visited before
        
        if verified[node]:
            return False # we have processed this node before and it does not start a cycle
        
        visited[node] = True
        for dstNode in edges.get(node,[]):
            if hasCycle(dstNode , visited , verified):
                return True
            else:
                verified[dstNode] = True
        
        # backtrack and set that the node is not visited
        visited[node] = False
        return False
            
    
    visited = [False] * len(nodes) # all nodes are not visited at the beginning
    verified = [False] * len(nodes) # all nodes which have been verified till now
    for node in nodes:
        if visited[node] == False:
            if hasCycle(node, visited , verified):
                return False
            
    return True # didn't find a cycle

#https://leetcode.com/problems/course-schedule/
if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0]]
    print(canFinish(numCourses , prerequisites))
    
