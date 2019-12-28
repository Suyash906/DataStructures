# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if None == l1 and None == l2:
            return None
        
        if None == l1:
            return l2
        
        if None == l2:
            return l1
        
        firstNode = False
        while l1 != None and l2!=None:
            if l1.val < l2.val:
                if False == firstNode:
                    p = res = ListNode(l1.val)
                    firstNode = True
                else:
                    p.next = ListNode(l1.val)
                    p = p.next
                l1=l1.next
            else:
                if False == firstNode:
                    p = res = ListNode(l2.val)
                    firstNode = True
                else:
                    p.next = ListNode(l2.val)
                    p = p.next
                l2=l2.next
        
        while l1 != None:
            if False == firstNode:
                p = res = ListNode(l1.val)
                firstNode = True
            else:
                p.next = ListNode(l1.val)
                p = p.next
            l1=l1.next
        
        while l2 != None:
            if False == firstNode:
                p = res = ListNode(l2.val)
                firstNode = True
            else:
                p.next = ListNode(l2.val)
                p = p.next
            l2=l2.next
            
        return res