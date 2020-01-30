# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root
        
        while curr!=None:
            if val == curr.val:
                return curr
            elif val > curr.val:
                if curr.right == None:
                    return None
                else:
                    curr = curr.right
            elif val < curr.val:
                if curr.left == None:
                    return None
                else:
                    curr = curr.left
        return None