
from typing import List , Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if len(preorder) == 1:
        return TreeNode(preorder[0])
    pre_index_map = {}
    for i in range(len(preorder)):
        pre_index_map[preorder[i]] = i
        
    in_index_map = {}
    for i in range(len(inorder)):
        in_index_map[inorder[i]] = i
        
    # generates a tree node based on the constrains
    def generate(inleft , inright):
        # base case
        if inleft < 0 or inleft > inright or inright == len(inorder):
            return None
        
        # base case. one node
        if inleft == inright:
            return TreeNode(inorder[inleft])
        
        values = inorder[inleft : inright + 1]
        rootIndex = len(inorder)
        for val in values:
            rootIndex = min(rootIndex, pre_index_map[val])
            
        root = TreeNode(preorder[rootIndex])
        root.left = generate(inleft , in_index_map[root.val] - 1)
        root.right = generate(in_index_map[root.val] + 1 , inright)
        return root
        
    
    root = TreeNode(preorder[0])
    root.left = generate(0 , in_index_map[root.val] - 1)
    root.right = generate(in_index_map[root.val] + 1 , len(inorder)  -1)
    return root
    
        
        
        
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/
if __name__ == "__main__":
    pass
