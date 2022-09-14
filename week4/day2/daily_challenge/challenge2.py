#Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

caractere = input("user's word: ")
n = len(caractere)
caractere=list(caractere.rstrip())
if n<2:
    print(''.join(caractere))
else:
    j=0
    for i in range(n):
        if (caractere[j]!=caractere[i]):
            j+=1
            caractere[j]=caractere[i]
    j+=1
    caractere = caractere[:j]        
print(caractere)

        