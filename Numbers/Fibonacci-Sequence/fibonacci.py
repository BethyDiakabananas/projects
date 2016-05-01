from math import sqrt

def fibonacci(n):
	"""Prints n numbers in a fibonacci sequence
	Formula Link: http://mathworld.wolfram.com/FibonacciNumber.html"""
	while n > 0:
		print int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
		n -= 1

def fibonacci_recursive(n):
	""""Prints n numbers in a fibonacci sequence recursively"""
	if n <= 1:
		return n
	else:
		return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = int(raw_input("Enter a number for a fibonacci sequence: "))
fibonacci(n)

n = int(raw_input("Enter a number for a fibonacci sequence done recursively: "))
while n > 0:
	print fibonacci_recursive(n)
	n -= 1
