def circumference(radius):
    """Calculate the circumference of a circle given its radius."""
    import math
    return 2 * math.pi * radius
r=int(input("Enter the radius of the circle: "))

print ("The circumference of the circle is:", circumference(r))
