def isPrime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if not x%i:
           return False
    return True

sum = 0
for i in range(1,2000000):
    if isPrime(i):
        sum += i
print sum 