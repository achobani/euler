a=0

def collatz(n):
    global a
    a += 1
    if n%2 == 0:
        n /= 2
        collatz(n)
    elif n == 1:
        return a
    else:
        n = 3*n + 1
        collatz(n)
    return a

largest = 0
num = 0
for i in range(1,1000000):
    a = 0
    x = collatz(i)
    if x > largest:
        largest = x
        num = i
print num
