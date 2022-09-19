import random
# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

number = 0
randomly = random.randint(1,100)
while int(number) < 1 or int(number) > 100:
       number= input("write a number betweeen 1 and 100: ")
if randomly == number:
    print("you success: {}=={}".format(randomly,number))
else:
    print("you lost  because {} is differente to {}".format(randomly,number))  
