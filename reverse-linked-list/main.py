from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    
    prev = None
    currHead = head
    while currHead: 
        nxt = currHead.next
        currHead.next = prev
        prev = currHead
        currHead = nxt
        
        
    return prev
        
    
                
                
#https://leetcode.com/problems/reverse-linked-list/submissions/
if __name__ == "__main__":
    pass


    
