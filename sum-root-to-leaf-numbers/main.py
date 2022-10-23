# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def sumNumbers(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    result = 0
    def dfs(node , currSum):
        nonlocal result
        if not node.left and not node.right:
            result += currSum * 10 + node.val
            return
        
        if node.left:
            dfs(node.left , currSum * 10 + node.val)
        if node.right:
            dfs(node.right , currSum * 10 + node.val)
        
    dfs(root , 0)
    return result
    


            
                
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
if __name__ == "__main__":
    pass


    
