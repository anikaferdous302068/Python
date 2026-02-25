# Take range input from user
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

# Create list of square values
squares = [num**2 for num in range(start, end + 1)]

# Separate even and odd square values
even_squares = [sq for sq in squares if sq % 2 == 0]
odd_squares = [sq for sq in squares if sq % 2 != 0]

# Display results
print("\nSquare values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)