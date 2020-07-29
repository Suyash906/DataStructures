class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for curr in preorder[1:]:
            if stack[-1].val > curr:
                stack[-1].left = TreeNode(curr)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < curr:
                    last = stack.pop()
                last.right = TreeNode(curr)
                stack.append(last.right)
        return root