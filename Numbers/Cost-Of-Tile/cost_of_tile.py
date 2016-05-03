def cost_of_tile(width, height, cost):
	area = width * height
	return round(area * cost, 2)

print "Thinking of tiling your room? We got you covered!"
width = int(raw_input("Enter the width (feet): "))
height = int(raw_input("Enter the height (feet): "))
cost = int(raw_input("Enter the cost per tile (square feet): "))

print "Cost of tiling: $" + str(cost_of_tile(width, height, cost))