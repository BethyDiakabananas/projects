def calculate_mortgage(months, rate, loan):
	monthly_rate = rate / 100 / 12
	payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan
	return payment

months = int(raw_input("Enter the payment period in months: "))
rate = int(raw_input("Enter the interest rate: "))
payment = int(raw_input("Enter the value of the loan: "))

print "The montly rate is: " + calculate_mortgage(months, rate, payment)

