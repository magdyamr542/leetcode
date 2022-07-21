from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if not headA or not headB:
        return None
    
    size_a = 1
    size_b = 1
    curr_head_a = headA
    while curr_head_a:
        curr_head_a = curr_head_a.next
        size_a += 1
        
    curr_head_b = headB
    while curr_head_b:
        curr_head_b = curr_head_b.next
        size_b += 1
        
    curr_head_a = headA
    curr_head_b = headB
    if size_a > size_b:
        diff = size_a - size_b
        while diff > 0 and curr_head_a:
            diff -= 1
            curr_head_a =  curr_head_a.next
    elif size_a < size_b:
        diff = size_b - size_a
        while diff > 0 and curr_head_b:
            diff -= 1
            curr_head_b =  curr_head_b.next
    
    while curr_head_a and curr_head_b:
        if curr_head_a == curr_head_b:
            return  curr_head_a
        curr_head_a = curr_head_a.next
        curr_head_b = curr_head_b.next
    
    
    return None
        

# https://leetcode.com/problems/intersection-of-two-linked-lists/
if __name__ == "__main__":
    pass
