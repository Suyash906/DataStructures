# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0
        res = None
        while l1 and l2:
            s = carry + l1.val + l2.val
            d  = s % 10
            carry = s // 10
            if not res:
                finalres = res = ListNode(d)
            else:
                res.next = ListNode(d)
                res = res.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            s = carry + l1.val
            d  = s % 10
            carry = s // 10
            res.next = ListNode(d)
            res = res.next
            l1 = l1.next
        
        while l2:
            s = carry + l2.val
            d  = s % 10
            carry = s // 10
            res.next = ListNode(d)
            res = res.next
            l2 = l2.next
        
        if 1 == carry:
            res.next = ListNode(1)
            
        return finalres
