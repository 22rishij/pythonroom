import turtle
a = turtle.Turtle()
sides = 99
length = 5
total = (sides - 2) * 180
interiorAngle = total / sides
angle = 180 - interiorAngle
numbers = range(0, sides)
print numbers 
colors = [ "blue", "red", "orange", "green", "yellow", "purple" ]
for thing in numbers:
	print thing
	a.forward(length)
	a.left(angle)
a.color("blue")
