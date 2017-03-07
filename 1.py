s = 0
for i in range(0,999):
        x = i % 3
        y = i % 5
        if x == 0 or y == 0:
            s = i + s
print s
