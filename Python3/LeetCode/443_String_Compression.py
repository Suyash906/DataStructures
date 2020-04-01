class Solution:
    def compress(self, chars: List[str]) -> int:
        anchor = write = 0
        for index, char in enumerate(chars):
            if index == len(chars)-1 or chars[index+1] != char:
                chars[write] = chars[anchor]
                write += 1
                if index > anchor: # This condition is true only if there are atleat two consecutive same charcters
                    for digit in str(index-anchor+1):
                        chars[write] = digit
                        write += 1
                anchor = index + 1
                
        return write
