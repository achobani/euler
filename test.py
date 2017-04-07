def collatz(n):
    if n%2 == 0:
        n /= 2
        collatz(n)
    elif n == 1:
        return "done"
    else:
        n = 3*n + 1
        collatz(n)

print collatz(13)
