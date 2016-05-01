def prime_factorization(n):
	"""Finds the prime factorization of a number that is 
	greater than or equal to 2"""
	prime_factors = []
	i = 2
	while i * i <= n:
		while (n % i) == 0:
			if i not in factors:
				prime_factors.append(i)
			n /= i
		i += 1
	if n > 1:
		prime_factors.append()
	return prime_factors

n = int(raw_input("Enter an integer to factor: "))
while n < 2:
	print "N must be greater than or equal to 2"
	n = int(raw_input("Enter a number to factor: "))
print prime_factorization(n)
