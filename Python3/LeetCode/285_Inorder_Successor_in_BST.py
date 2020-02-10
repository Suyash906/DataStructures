# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMin(self, root: 'TreeNode') -> 'TreeNode':
        while root.left!=None:
            root = root.left
        return root
        
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        # case 1 node to be searched is null
        if None == p or None == root:
            return None
        
        # case 2 the node has  the right child, find the leftmost node of right child
        if None != p.right:
            return self.findMin(p.right)
        else: #case 3 the node has no right child, find the deepest ances
            ancestor = root
            successor = None
            while ancestor != p:
                if ancestor.val > p.val:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            return successor
        return None
        
