def palindrome(n):
    num = n
    rev = 0
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num / 10
    if(rev == n):
        return True
    else:
        return False

def multiply():
    largest = 0
    for i in range(100,999+1):
        for j in range(100,999+1):
            if(palindrome(i*j)):
                if (i*j > largest):
                    largest = i*j
    return largest

print multiply()