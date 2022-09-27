#  Exercise 2: Random Module
import random
''' Create a function that accepts a number between 1 and 100,
    then rolls a random number between 1 and 100,
    if it’s the same number, display a success
    message to the user, else don’t.
'''

def my_function():
    num = 0
    
    while num < 1 or num > 100:
        num = int(input("write a numer between 1 and 100: "))
    if num==random.randint(1,100):
        print("you get success")
    else:
        print("you lost")
    


my_function()