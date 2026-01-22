import turtle
turtle.Screen().bgcolor("purple")
turtle.Screen().setup(500,500)
Square = turtle.Turtle()
num_sides=4
side_length=100
angle=360.0/num_sides
for i in range(num_sides):
    Square.forward(side_length)
    Square.right(angle)
turtle.done()