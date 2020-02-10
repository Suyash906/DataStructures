# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBSTUtil(self, root: TreeNode, minValue, maxValue) -> bool:
        if None == root:
            return True
        if root.val > minValue and root.val < maxValue and self.isValidBSTUtil(root.left, minValue, root.val) and self.isValidBSTUtil(root.right, root.val, maxValue):
            return True
        return False
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTUtil(root, -2147483649 , 2147483648)
