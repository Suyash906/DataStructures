class Solution:
    def peek_stack(self, stack):
        if stack:
            return stack[-1]
        else:
            return None
    
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if ')' == char and len(stack) > 0 and '(' == self.peek_stack(stack):
                stack.pop()
            elif '}' == char and len(stack) > 0 and '{' == self.peek_stack(stack):
                stack.pop()
            elif ']' == char and len(stack) > 0 and '[' == self.peek_stack(stack):
                stack.pop()
            else:
                stack.append(char)
        return True if len(stack) == 0 else False