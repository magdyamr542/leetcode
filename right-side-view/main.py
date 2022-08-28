from typing import List , Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    # do a depth traversal with a bfs and at each stage append the most right element
    if not root:
        return []
    queue = [root]
    result = []
    while len(queue) > 0:
        curr_queue = queue
        queue = []
        if len(curr_queue) > 0:
            result.append(curr_queue[len(curr_queue) - 1].val)
        for node in curr_queue:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
            
        
        
                
                
# https://leetcode.com/problems/binary-tree-right-side-view/submissions/
if __name__ == "__main__":
    print(rightSideView(None))


    
