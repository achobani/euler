def sumOfDigits(n):
    x = n
    arr = []
    while len(str(x)) > 1:
        arr.append(x%10)
        x = x//(10)
    arr.append(x)
    print sum(arr)

def factorial(n):
    x = n
    for i in range(1,n):
        x *= i
    return x

sumOfDigits(factorial(100))
