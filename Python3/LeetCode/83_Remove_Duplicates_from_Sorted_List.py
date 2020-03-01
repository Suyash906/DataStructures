# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if None == head or None == head.next:
            return head
        
        prev = head
        curr = head.next
        
        while curr is not None:
            if prev.val == curr.val:
                prev.next = curr.next
                curr = prev.next
            else:
                curr = curr.next
                prev = prev.next
        
        return head
