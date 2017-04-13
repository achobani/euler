x = 2**1000
arr = []
while len(str(x)) > 1:
    arr.append(x%10)
    x = x//(10)
arr.append(x)
print sum(arr)
