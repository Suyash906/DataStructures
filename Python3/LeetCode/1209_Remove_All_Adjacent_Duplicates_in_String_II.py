class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        char_stack = []
        count_stack = []
        prev = 0
        curr = 0
        while curr < len(s):
            if not char_stack:
                char_stack.append(s[curr])
                count_stack.append(1)
            elif char_stack[-1] != s[curr]:
                char_stack.append(s[curr])
                count_stack.append(1)
            elif count_stack[-1]+1 == k:
                for i in range(k-1):
                    char_stack.pop()
                count_stack.pop()
            else:
                count_stack[-1] = count_stack[-1] + 1
                char_stack.append(s[curr])
            curr+=1
        return "".join(char_stack)
