def reverseStringLeetCode(s):
    start = 0
    end = len(s)-1
    1
    while start < end:
        s[start],s[end] = s[end], s[start]
        start+=1
        end -=1
    s = "".join(s)
    return s

def reverseStringEasy(s):
    reversed_string = ''
    for char in reversed(s):
        reversed_string+=char
    return reversed_string

def reverseString(s):
    end = len(s)-1
    reversed_string = ''

    while end >=0:
        reversed_string += s[end]
        end-=1
    return reversed_string

res = reverseString('alice')
print(res)

res = reverseStringEasy('alpha')
print(res)

res = reverseStringLeetCode([c for c in 'leetcode'])
print(res)