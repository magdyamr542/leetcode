# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        biggest = root.val
        def dfs(node):
            nonlocal biggest
            if not node.left and not node.right:
                return node.val 

            left = -10001
            right = -10001
            if node.left:
                left = dfs(node.left)

            if node.right:
                right = dfs(node.right)

            biggest = max(biggest , left , right , node.val , left + node.val  ,  right + node.val , left + right + node.val)


            return max(node.val , node.val + left , node.val + right)


        dfs(root)
        return biggest 

# https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/
if __name__ == "__main__":
    pass
