import math

def pi(n):
	"""Calculates PI based on the number of digits"""
	return '%.*f' % (n, math.pi)

n = int(raw_input("Enter the number of digits for pi: "))
while n > 50:
	print "n must below 50"
	n = int(raw_input("Enter the number of digits for pi: "))
print pi(n)
