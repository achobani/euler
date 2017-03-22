def isPrime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if not x%i:
           return False
    return True

counter = 0
i = 2
while counter < 10001:
    if isPrime(i):
        counter += 1
    i += 1
print i-1