#Exercice6
#Write a function that returns factorial of a number
factorial= lambda nbr: nbr*factorial(nbr-1) if nbr!=0 else 1
print(factorial(7))