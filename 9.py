a = 0
b = 0
c = 0
m = 2
while True:
    for n in range(1, m):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if (a+b+c)==1000:
            print a*b*c
            break
    m += 1