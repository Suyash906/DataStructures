def findFactorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial*=i
    return factorial
print(findFactorial(5))
print(findFactorial(10))