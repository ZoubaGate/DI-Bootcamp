import random
 #exercice daily_challenge

x = input("saisir un mot de 10 lettre: ")
if len(x) < 10:
    print("votre mot n'a pas atteind les 10 caractere")
if len(x) > 10:
    print("votre mot a depasser les 10 caractere")
print("La 1er lettre du mot saisie est: ",x[0]);
print("La dernier lettre du mot saisie est: ",x[-1])

#3
print("The users enters {}".format(x))
print("Then, you have to construct the string character by character")
size = len(x)

for i in range(len(x)):
    print(x[:i+1])

#4 Swap some characters around then print the newly jumbled string
l = list(x)
random.shuffle(l)
x= ''.join(l)
print("Affter using saple we are: ",x)
