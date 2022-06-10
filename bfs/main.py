from collections import deque

# graph is a dict that indicates which node can access which other nodes
def bfs(graph , start_node):
    visited = set()
    q = deque()
    q.append(start_node)
    while q:
        node = q.popleft()
        if not node in visited:
            visited.add(node)
            print("visit" , node)
            neighbors = graph.get(node , [])
            for n in neighbors:
                if n not in visited:
                    q.append(n)


def dfs(graph , start_node):
    visited = set()

    def do_dfs(node):
        print("visit" , node)
        visited.add(node)
        neighbors = graph.get(node , [])
        for n in neighbors:
            if n not in visited:
                do_dfs(n)
    do_dfs(start_node)



#      A
#    /  \
#   B    C
#  / \    \
# D   E____F   

def main():
    graph = {
        "A" : ["B" , "C"],
        "B" : ["D" , "E" ,],
        "C" : ["F"],
        "E" : ["F"],
    }
    print("bfs")
    bfs(graph , "A")
    print("dfs")
    dfs(graph , "A")

if __name__ == "__main__":
    main()
