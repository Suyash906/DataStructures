# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestorHelper(self, root, p, q):
        ## base
        if not root:return (0, None)
        
        
        ## body
        nodes_found_count = 0
        
        count, left = self.lowestCommonAncestorHelper(root.left, p, q)
        if left:return (nodes_found_count, left)
        nodes_found_count += count
        
        count, right = self.lowestCommonAncestorHelper(root.right, p, q)
        if right:return (nodes_found_count, right)
        nodes_found_count += count
        
        if root == p or root == q:
            nodes_found_count += 1
        
        lca = root if nodes_found_count == 2 else None
        
        return (nodes_found_count, lca)
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nodes_found_count, lca =  self.lowestCommonAncestorHelper(root, p, q)
        return lca
