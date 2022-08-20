from typing import Optional , List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def genRec(nums):
        # base case
        if len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = genRec(nums[0 : mid])
        node.right = genRec(nums[mid+1:])
        return node
    
    return genRec(nums)
        
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
def main():
    pass

if __name__ == "__main__":
    main()
