# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addOne(self, l, prev):
        if l == prev:
            s = l.val+1
            l.val = s % 10
            carry = s // 10
            return carry
        carry = self.addOne(l.next, prev)
        s = carry + l.val
        l.val = s % 10
        carry = s // 10
        return carry
            
    def addTwoNumbersUtil(self, p, q, flag):
        if not p.next and not q.next:
            s = p.val + q.val
            if 1 == flag:
                p.val = s % 10
            else:
                q.val = s % 10
            carry = s // 10
            return carry
        carry = self.addTwoNumbersUtil(p.next,q.next,flag)
        s = carry + p.val + q.val
        if 1 == flag:
            p.val = s % 10
        else:
            q.val = s % 10
        carry = s // 10
        return carry
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        
        m, n = 0, 0
        p, q = l1, l2
        while p:
            m+=1
            p = p.next
        
        while q:
            n+=1
            q = q.next
        
        p, q = l1, l2
        flag = 1
        if m > n:
            c = m-n
            while c != 0:
                prev = p
                p = p.next
                c-=1
        else:
            c = n - m
            flag =2
            while c != 0:
                prev = q
                q = q.next
                c-=1
                
        carry = self.addTwoNumbersUtil(p,q, flag)
        
        if 0 == carry:
            return l1 if flag == 1 else l2
        
        if flag == 1:
            if m!=n:
                carry = self.addOne(l1, prev)
            if 0 == carry:
                return l1
            else:
                new_node = ListNode(1)
                temp = l1
                new_node.next = temp
                l1 = new_node
                return l1
        else:
            if m!=n:
                carry = self.addOne(l2, prev)
            if 0 == carry:
                return l2
            else:
                new_node = ListNode(1)
                temp = l2
                new_node.next = temp
                l2 = new_node
                return l2
