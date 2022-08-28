class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root: TreeNode) -> int:
    result = 0
    def dfs(node, currMax):
        nonlocal result
        if not node:
            return
        
        if node.val >= currMax:
            result += 1
        
        dfs(node.left , max(node.val , currMax))
        dfs(node.right , max(node.val , currMax))
        
    dfs(root , root.val)
    return result
        
    
            
                
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
if __name__ == "__main__":
    pass


    
