# To print something to the screen:
# Python ignores spaces.  
print("Hello World!")
# String in python can either be inside single qoute or double qoute: 
print('Hello Wrold!') 
# Print numbers:
print(100)
# Variables:
# Declaring a variable:
# => score is the variable, 
# => = is the assignment operator. 
# => 800 is the value of score. 
score = 800 
print(score)
# Conditional Expressions:
# => Boolean Expressions => gives True or False. 
# Python Statement: 
# => if expression: statement
having_fun = "Yes"
# Equality operator: ==
if (having_fun == "Yes"):
    print("Glad you are having Fun ! ")
# DRY => Don't Repeat Yourself. 
# Using Functions:
# def => defines the function. 
def say_hi(name):
    print(f"Hello, {name}!")
# Call the function:
say_hi("Khawlah")
# Creating a Class:
class Puppy():
    # init => assigns values to any variables in the class
    # self => how to refer the current instance of a class 
    def __init__(self, name, favorite_toy ):
        self.name = name
        self.favorite_toy = favorite_toy
    def play(self):
        print(self.name + " is playing with the "+ self.favorite_toy)
# Create instance of the class:
marble = Puppy('Marble', 'teddy bear')
onyx = Puppy('onyx', 'lizard')
# Call the methods in the class:
marble.play()
onyx.play()

