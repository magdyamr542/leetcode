from typing import List , Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    queue = [root]
    result = []
    while len(queue) > 0:
        curr_level = []
        curr_queue = queue
        queue = []
        for node in curr_queue:
            curr_level.append(node.val)
        result.append(curr_level)
            
        for node in curr_queue:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
            
    return result
                
                
#https://leetcode.com/problems/binary-tree-level-order-traversal/
if __name__ == "__main__":
    print(levelOrder(None))


    
