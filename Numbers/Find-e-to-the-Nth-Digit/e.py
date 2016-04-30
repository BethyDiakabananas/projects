import math

def e(n):
	"""Calculates E based on the number of digits"""
	return '%.*f' % (n, math.e)

n = int(raw_input("Enter the number of digits for e: "))
while n > 50:
	print "n must below 50"
	n = int(raw_input("Enter the number of digits for e: "))
print e(n)

