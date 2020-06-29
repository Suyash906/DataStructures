# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:return []
        res = []
        q = deque([(root,0)])
        while q:
            curr, level= q.popleft()
            if level == len(res):
                res.append(curr.val)
            else:
                res[level] = max(res[level], curr.val)
            if curr.left:
                q.append((curr.left,level+1))
            if curr.right:
                q.append((curr.right,level+1))
        return res
