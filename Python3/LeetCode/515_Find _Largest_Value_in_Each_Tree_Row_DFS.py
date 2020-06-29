# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root, depth):
            nonlocal res
            if root is None:
                return
            
            if depth == len(res):
                res.append(root.val)
                
            res[depth] = max(res[depth], root.val)
            
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root, 0)
        return res
