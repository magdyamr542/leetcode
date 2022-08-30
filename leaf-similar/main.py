from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        leafs1 = []
        leafs2 = []
        def dfs(node , nodesList):
            if not node:
                return 
            if not node.left and not node.right:
                nodesList.append(node.val)
                return 
            dfs(node.left , nodesList)
            dfs(node.right , nodesList)
            
        dfs(root1 , leafs1)
        dfs(root2 , leafs2)
        if len(leafs1) != len(leafs2):
            return False
        
        for i in range(len(leafs1)):
            if leafs1[i] != leafs2[i]:
                return False
            
        return True
        
        
                
                
# https://leetcode.com/problems/leaf-similar-trees/solution/
if __name__ == "__main__":
    pass


    
