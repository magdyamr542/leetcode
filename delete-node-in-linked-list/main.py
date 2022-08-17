from typing import List , Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # keep shifting the values to the left
        currNode = node
        while currNode and currNode.next:
            currNode.val = currNode.next.val
            if not currNode.next.next:
                currNode.next = None
                return
            currNode = currNode.next
        
                
                
# https://leetcode.com/problems/delete-node-in-a-linked-list
if __name__ == "__main__":
    pass


    
