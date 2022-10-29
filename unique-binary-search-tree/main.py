def numTrees(n: int) -> int:
    cache = {}
    for i in range(1,n+1):
        cache[(i,i)] = 1 # num combs with one node is 1
    
    def dfs(currNodes):
        if len(currNodes) <= 2:
            return len(currNodes) # 1 or 2 nodes make 1 or 2 combinations
        
        if cache.get((currNodes[0],currNodes[-1]), None):
            return cache[(currNodes[0],currNodes[-1])] # we already computed this before for the curr list
        
        result = 0
        for i in range(len(currNodes)):
            left = currNodes[:i]
            right = currNodes[i+1:]
            fromLeft = dfs(left)
            fromRight = dfs(right)
            if len(left) and len(right):
                result += fromLeft * fromRight
            else:
                result += max(fromLeft,fromRight)
        cache[(currNodes[0],  currNodes[-1])] = result
        return result
    
    return dfs([i for i in range(1,n+1)])
            
                
                
# https://leetcode.com/problems/unique-binary-search-trees/
if __name__ == "__main__":
    print(numTrees(5))
    
