### Factorial
```
def findFactorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial*=i
    return factorial
```

### Fibinacci
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
