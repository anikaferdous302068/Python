def due(paid,bill):
    return (paid-bill)
x=int(input("Enter the amount paid: "))
y=int(input("Enter the bill amount: "))
print("The due amount is:",due(x,y))
