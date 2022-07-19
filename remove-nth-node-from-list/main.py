
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy_head = ListNode(-1 , head)
        left = dummy_head
        right  = head
        for i in range(n):
            if right:
                right = right.next
        
        while right:
            right = right.next
            left = left.next
            
        left.next = left.next.next
        
        return dummy_head.next
            
        
        
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
if __name__ == "__main__":
    head = ListNode(1 , ListNode(2 , ListNode(3 , ListNode(4))))
    n = 2
    print(f"before removing {n} " , head)
    print("after" , removeNthFromEnd(head , n))
