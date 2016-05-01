from math import sqrt

def fibonacci(n):
	"""Prints n numbers in a fibonacci sequence
	Formula Link: http://mathworld.wolfram.com/FibonacciNumber.html"""
	while n > 0:
		print int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
		n -= 1
	return 1

n = int(raw_input("Enter a number for a fibonacci sequence: "))
print fibonacci(n)
