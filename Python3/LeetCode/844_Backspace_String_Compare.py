class Solution:
    def processStack(self, string, stack):
        for char in string:
            if '#' == char and len(stack) > 0:
                stack.pop()
            else:
                stack.append(char)
    
    def trimHash(self, stack):
        for i, curr in enumerate(stack):
            if '#' == curr:
                del stack[i]
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_1 = []
        stack_2 = []
        
        self.processStack(S, stack_1)
        self.processStack(T, stack_2)
        
        self.trimHash(stack_1)
        self.trimHash(stack_2)
        
        if len(stack_1) != len(stack_2):
            return False
        for i in range(len(stack_1)):
            if stack_1[i] != stack_2[i]:
                return False
        return True