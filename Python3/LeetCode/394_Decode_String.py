# The number can be more than 9 so need to take care of the digits
# The curr_num is used to track the number corresponding to curr_string
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ''
        curr_num = 0
        for char in s:
            if char == '[':
                stack.append(curr_string)
                stack.append(curr_num)
                curr_string = ''
                curr_num = 0
            elif char == ']':
                num = stack.pop()
                prev_string = stack.pop()
                curr_string = prev_string + (curr_string * num)
            elif char.isdigit():
                curr_num = (curr_num * 10) + int(char)
            else:
                # If the character is not within the square bracket then also it is added on to the 
                curr_string += char
        return curr_string
        
