def fibonacci(n):
	""""Prints n numbers in a fibonacci sequence"""
	while n > 0:
		return fibonacci(n-1) + fibonacci(n-2)
		n -= 1
	return `

n = int(raw_input("Enter a number for a fibonacci sequence: "))
print fibonacci(n)
