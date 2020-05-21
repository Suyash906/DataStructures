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

print(printFibonacci(0))
print(printFibonacci(1))
print(printFibonacci(2))
print(printFibonacci(3))
print(printFibonacci(5))
print(printFibonacci(10))