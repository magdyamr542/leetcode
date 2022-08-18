from typing import List , Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    def dfs(currRoot):
        # base cases
        if not currRoot:
            return None , []
        
        if not currRoot.left and not currRoot.right:
            if currRoot.val == p.val or currRoot.val == q.val:
                return None , [currRoot.val]
            return None , []
        
        
        fromLeft , leftValues = dfs(currRoot.left)
        if fromLeft:
            return fromLeft , []
        
        
        fromRight , rightValues = dfs(currRoot.right)
        if fromRight:
            return fromRight , []
        
        if len(leftValues) == 1 and len(rightValues) == 1:
            return currRoot , []
        
        if len(leftValues) == 1:
            if ((leftValues[0] == p.val and currRoot.val == q.val) or (leftValues[0] == q.val and currRoot.val == p.val)):
                return currRoot , []
            else:
                return None , leftValues
        
        if len(rightValues) == 1:
            if((rightValues[0] == p.val and currRoot.val == q.val) or (rightValues[0] == q.val and currRoot.val == p.val)):
                return currRoot , []
            else:
                return None , rightValues
        
            
        if currRoot.val == p.val or currRoot.val == q.val:
            return None , [currRoot.val]
            
        return None , []
            
        
    node , _ =  dfs(root)
    return node 
        
                
                
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
if __name__ == "__main__":
    pass


    
