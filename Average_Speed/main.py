a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
c = int(input("Enter c value:"))
average = (a + b + c) / 3
print("The average is:", average)
if average > a and average > b and average > c:
    print("%d is higher than %d, %d and %d" % (average, a, b, c))
elif average > a and average > b:
    print("%d is higher than %d and %d" % (average, a, b))
elif average > a and average > c:
    print("%d is higher than %d and %d" % (average, a, c))
elif average > b and average > c:
    print("%d is higher than %d and %d" % (average, b, c))
elif average > a:
    print("%d is higher than %d" % (average, a))
elif average > b:
    print("%d is higher than %d" % (average, b))
elif average > c:
    print("%d is higher than %d" % (average, c))
else:
    print ("Invalid input") 
    