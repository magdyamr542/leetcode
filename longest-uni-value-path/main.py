from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestUnivaluePath(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    longest = 0
    def dfs(node):
        nonlocal longest
        if not node.left and not node.right:
            return node.val , 0
        
        currResult = 0
        leftFreq = 0
        rightFreq = 0
        left = None
        right = None
        if node.left:
            left , leftFreq = dfs(node.left)
            if node.val == left:
                currResult += (leftFreq + 1)
                
            
        if node.right:
            right , rightFreq = dfs(node.right)
            if node.val == right:
                currResult += (rightFreq + 1)
        
        if currResult > longest:
            longest = currResult
            
            
        if left is not None and right is not None and node.val == left and left == right:
            return node.val , max(leftFreq , rightFreq) + 1
      
        if left is not None and node.val == left:
            return node.val , leftFreq  + 1
        
        if right is not None and node.val == right:
            return node.val , rightFreq  + 1
       
        return node.val , 0
        
    
    dfs(root)
    return longest 
        
            
# https://leetcode.com/problems/longest-univalue-path/
if __name__ == "__main__":
    pass


    
