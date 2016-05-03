def next_prime_number(n):
	is_prime = False
	while is_prime == False:
		n += 1
		is_prime = True
		for i in prime_numbers:
			if n % i == 0:
				is_prime = False
		if is_prime == True:
			prime_numbers.append(n)
			return n

prime_numbers = [2]
next_prime = True
n = 1

print "2 is the first prime number."
while next_prime == True:
	answer = raw_input("Would you like to see the next prime number? (y/n) ")
	if answer.lower() == "y":
		n = next_prime_number(n)
		print "%d is the next prime number" % (n)
		next_prime = True
	else:
		print "See you next time!"
		next_prime = False


