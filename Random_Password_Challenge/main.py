import random
import string

# define characters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits

# combine all characters
characters = lower + upper + num

# choose random characters
password = list(random.choice(characters) for i in range(10))

# shuffle the password
random.shuffle(password)

# convert list to string
password = "".join(password)

print("Random Password:", password)