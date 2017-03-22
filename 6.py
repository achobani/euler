def sum_of_squares(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**2
    return sum

def square_of_sums(n):
    sum = 0
    square = 0
    for i in range(1,n+1):
        sum = sum + i
        square = sum **2
    return square

ans = square_of_sums(100) - sum_of_squares(100)
print ans