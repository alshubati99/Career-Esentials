# importing the random module
import random

# Create a list of numbers:
numbers = [1,2,3,4,5,8,10]
# shuffle numbers
random.shuffle(numbers)
print(numbers)

# choice numbers
number = random.choice(numbers)
print(number)

