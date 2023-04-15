from typing import List , Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
            return []
    # all nodes in the same curr_level belong together in the output inside of an array
    
    queue = [[root , 0]] # a tuple [node, curr_level]
    curr_level = -1 # current level being processed now
    
    result = []
    while queue:
        curr_node , curr_node_level = queue.pop(0)
        
        if curr_node_level == curr_level:
            # we already created an array for this level. just append the current node's value to it
            result[-1].append(curr_node.val)
        else:
            # we are processing a new level
            curr_level = curr_node_level
            result.append([curr_node.val])
            
        if curr_node.left:
            queue.append([curr_node.left, curr_level + 1])
        if curr_node.right:
            queue.append([curr_node.right, curr_level + 1])

    return result
                
                
#https://leetcode.com/problems/binary-tree-level-order-traversal/
if __name__ == "__main__":
    print(levelOrder(None))


    
