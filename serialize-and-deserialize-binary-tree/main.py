class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    # use preorder traversal
    def preorder(currNode):
        if not currNode:
            return "N"
        return f"{currNode.val},{preorder(currNode.left)},{preorder(currNode.right)}"
    
    return preorder(root)
    

def deserialize(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    # 1,2,n,n,3,4,n,n,5,n,n
    if len(data) == 1:
        return None
    nodes = data.split(",")
    pointer = 0
    root = TreeNode(-1)
    
    def dfs(currIndex):
        # base cases
        if currIndex >= len(nodes):
            return None , currIndex
        if nodes[currIndex] == "N":
            return None , currIndex + 1
        
        node = TreeNode(nodes[currIndex])
        left , currIndex = dfs(currIndex + 1)
        node.left = left
        right , currIndex = dfs(currIndex)
        node.right = right
        return node , currIndex 
    
    result , _  = dfs(0)
    return result
    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
            
                
                
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
if __name__ == "__main__":
    pass
    
