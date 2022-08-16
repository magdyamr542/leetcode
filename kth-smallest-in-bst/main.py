from typing import List , Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    values = []
    # do a preorder traversal and return the nth node
    def preorder(node):
        if node.left:
            if preorder(node.left):
                return True
           
        values.append(node.val)
        if len(values) == k:
            return True 
            
        if node.right:
            if preorder(node.right):
                return True
            
            
    preorder(root)
    return values[k-1]
    
            
                
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
if __name__ == "__main__":
    pass


    
