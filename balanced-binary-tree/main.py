from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def getHeight(node):
            # base code
            if not node.left and not node.right:
                return 1
            
            hl = 0
            if node.left:
                hl = getHeight(node.left)
                
            hr = 0
            if node.right:
                hr = getHeight(node.right)
            
            # -1 means the height diff is not allowed. bigger than 1
            if hl == -1 or hr == -1:
                return -1
          
            if hl - hr > 1 or hr - hl > 1:
                return -1
            
            return max(hl , hr) + 1
                
            
        return getHeight(root) != -1
            
        
        
# https://leetcode.com/problems/balanced-binary-tree/
if __name__ == "__main__":
    pass
