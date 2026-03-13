import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Taking input
r = float(input("Enter the radius of the circle: "))

# Creating object
c = Circle(r)

# Display results
print("Area of the circle:", round(c.area(), 2))
print("Perimeter of the circle:", round(c.perimeter(), 2))