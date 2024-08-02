def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, n):
        if n % i == 0:
            return False
    return True

def print_primes_less_than(limit):
  
    for num in range(2, limit):
        if is_prime(num):
            print(num)
try:
	inplimit = int(input("Enter Limit till which To Calculate Primes : "))
	print_primes_less_than(inplimit)
	
exept Exeption as e:
	print(e)
