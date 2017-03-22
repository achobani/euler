def isPrime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if not x%i:
           return False
    return True

def largest_factor(number):
    max_val = 0
    for i in range (2, int(number**0.5)+1):
	    if isPrime(i):
	        while number%i == 0:
	        	number = number/i
	        	if (i > max_val):
	        		max_val = i
	       	i += 1
    return max_val

print largest_factor(600851475143)