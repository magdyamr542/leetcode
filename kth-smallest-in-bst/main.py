from typing import List , Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    values = []
    # do a inorder traversal and return the nth node
    def inorder(node):
        if node.left:
            if inorder(node.left):
                return True
           
        values.append(node.val)
        if len(values) == k:
            return True 
            
        if node.right:
            if inorder(node.right):
                return True
            
            
    inorder(root)
    return values[k-1]
    
            
                
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
if __name__ == "__main__":
    pass


    
