def tri(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

def factor(n):
    a = 0
    for i in range(1,int(n**.5)+1):
        if (n%i == 0):
            a += 2
    return a

i = 1
bool = True
while bool:
    n = tri(i)
    if factor(n) > 500:
        print n
        bool = False
    i+= 1
