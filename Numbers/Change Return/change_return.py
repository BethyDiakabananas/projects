from math import floor 

def calculate_change(cost, given):
	twenties, tens, fives, ones, quarters, dimes, nickles, pennies = 0, 0, 0, 0, 0, 0, 0, 0
	d = given - cost
	dollars = int(floor(d))
	coins = int(d - floor(d) * 100)
	if dollars > 0:
		twenties = dollars / 20
		tens = (dollars % 20) / 10
		fives = (dollars % 10) / 5
		ones = dollars % 5
	if coins > 0:
		quarters = dollars / 25
		dimes = (dollars % 25) / 10
		nickles = (dollars % 10) / 5
		pennies = dollars % 5
	print "Your change is $%.2f: \n \
			%.0f twenties \n \
			%.0f tens \n \
			%.0f fives \n \
			%.0f ones \n \
			%.0f quarters \n \
			%.0f dimes \n \
			%.0f nickels \n \
			%.0f pennies" % (d, twenties, tens, fives, ones, quarters, dimes, nickles, pennies)

cost = int(raw_input("How much was the item? $"))
given = int(raw_input("How much did you pay? $"))
while given < cost:
	print "You still owe $%.2f" % (cost - given)
	given = float(raw_input("Enter amount given: "))

calculate_change(cost, given)