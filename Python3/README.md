### String Functions
- **find()** - Where in the text is the word "welcome"?:
```
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x) # 7
```
- **capitalize()** - Capitalize first charatcter
```
s = "sector seven"
res = s.capitalize()
print(res) # Sector seven
```
- **count()** - Return the number of times the value "apple" appears in the string:
```
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x) # 2
```
- **upper()** - Convert string to upper case
```
txt = "Hello my friends"
x = txt.upper()
print(x) # HELLO MY FRIENDS
```
- **isupper()** - checks if string is in upper case
```
txt = "THIS IS NOW!"
x = txt.isupper()
print(x) # True
```
- **replace()** - Replace the word
```
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x) # I like apples
```
- **join()** - Join all items of a tuple or a list
```
myTuple = ("John", "Peter", "Vicky")
x = "&".join(myTuple)
print(x) # John&Peter&Vicky
```
### Factorial
```
def findFactorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial*=i
    return factorial
```

### Fibonacci
```
def printFibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    
    fib = [0, 1]
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib
```
### Replace all occurences of a single character in a string
```
def replaceString(input, search_char, replace_char):
    result = ''
    for char in input:
        if char == search_char:
            result += replace_char
        else:
            result += char
    return result
```

### Replace only first occurence of the a single character in a string
```
def replaceFirstOccurenceString(input, search_char, replace_char):
    result = ''
    first_char_replaced = False
    for char in input:
        if not first_char_replaced and char == search_char:
            result += replace_char
            first_char_replaced = True
        else:
            result += char
    return result
```

### Reverse String
```
def reverseString(s):
    end = len(s)-1
    reversed_string = ''

    while end >=0:
        reversed_string += s[end]
        end-=1
    return reversed_string
```
### Reverse String - Easy
```
def reverseStringEasy(s):
    reversed_string = ''
    for char in reversed(s):
        reversed_string+=char
    return reversed_string
```

### Reverse String - Leetcode
```
def reverseStringLeetCode(s):
    start = 0
    end = len(s)-1
    while start < end:
        s[start],s[end] = s[end], s[start]
        start+=1
        end -=1
    return s
```


