# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder is None or len(preorder) <= 0:
            return None
        
        
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, len(preorder)):
            curr_node = TreeNode(preorder[i])
            if inorder_map[curr_node.val] < inorder_map[stack[-1].val]:
                stack[-1].left = curr_node
            else:
                parent = TreeNode()
                while stack and inorder_map[curr_node.val] > inorder_map[stack[-1].val] :
                    parent = stack.pop()
                parent.right = curr_node
            stack.append(curr_node)
        return root
