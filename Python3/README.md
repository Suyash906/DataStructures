### Python Generators
```python
def foo():
    for i in range(10):
        yield i

x = foo()

## first 3 values
print('  first 3 values  ')
for i in range(3):
    print(x.__next__())

print('  next 3 values  ')
## next 3 values
for i in range(3):
    print(x.__next__())
```

### Process Input
```python
import re
def process_input(s):
  s = s.strip()
  s = re.split(' +', s)
  return s

s = '   63 41    92  81            69  70   '
x = process_input(s)
print(x)
```

### Glocal variable(nonlocal)
```python
def outside():
  x = 0
  def inside():
    nonlocal x
    x+=1
    print(x) # 1
  inside()
  x+=1
  print(x) # 2
outside()
```
### Sort a list
```python
dictionary = {'c': 3, 'b': 3, 'aa': 2, 'a': 2, 'x':5}

## sort by frequency
sorted_dictionary = sorted(dictionary, key=lambda key:-dictionary[key])
print(sorted_dictionary)  # ['x', 'c', 'b', 'aa', 'a']

## sort in lexicographical
sorted_dictionary = sorted(dictionary, key=lambda key:key)
print(sorted_dictionary) # ['a', 'aa', 'b', 'c', 'x']

## sort by frequency and then lexicographicaly 
sorted_dictionary = sorted(dictionary, key=lambda key: (-dictionary[key], key))

print(sorted_dictionary) # ['x', 'b', 'c', 'a', 'aa']
 
## sort lexicographicaly and then by frequency 
sorted_dictionary = sorted(dictionary, key=lambda key: (key, -dictionary[key]))

print(sorted_dictionary) # ['a', 'aa', 'b', 'c', 'x']
```

### String Functions
- **find()** - Where in the text is the word "welcome"?:
```python
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x) # 7
```
- **capitalize()** - Capitalize first charatcter
```python
s = "sector seven"
res = s.capitalize()
print(res) # Sector seven
```
- **count()** - Return the number of times the value "apple" appears in the string:
```python
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x) # 2
```
- **upper()** - Convert string to upper case
```python
txt = "Hello my friends"
x = txt.upper()
print(x) # HELLO MY FRIENDS
```
- **isupper()** - checks if string is in upper case
```python
txt = "THIS IS NOW!"
x = txt.isupper()
print(x) # True
```
- **replace()** - Replace the word
```python
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x) # I like apples
```
- **join()** - Join all items of a tuple or a list
```python
myTuple = ("John", "Peter", "Vicky")
x = "&".join(myTuple)
print(x) # John&Peter&Vicky
```
### Factorial
```python
def findFactorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial*=i
    return factorial
```

### Fibonacci
```python
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
```python
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
```python
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
```python
def reverseString(s):
    end = len(s)-1
    reversed_string = ''

    while end >=0:
        reversed_string += s[end]
        end-=1
    return reversed_string
```
### Reverse String - Easy
```python
def reverseStringEasy(s):
    reversed_string = ''
    for char in reversed(s):
        reversed_string+=char
    return reversed_string
```

### Reverse String - Leetcode
```python
def reverseStringLeetCode(s):
    start = 0
    end = len(s)-1
    while start < end:
        s[start],s[end] = s[end], s[start]
        start+=1
        end -=1
    return s
```


