# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        if None == head:
            return None
        
        while head.val == val:
            head = head.next
            if head is None:
                return None
        
        prev = head
        curr = head.next
        
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                curr = curr.next
                prev = prev.next
        
        return head
