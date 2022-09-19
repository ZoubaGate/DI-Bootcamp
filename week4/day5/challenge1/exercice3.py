#Exercice 3:
#Write a script that calculates the number of upper case letters and lower case letters in a string.
def my_string(s):
    d={"NbrUpper":0,"NbrLower":0}
    for c in s:
        if c.isupper():
            d["NbrUpper"]+=1
        if c.islower():
            d["NbrLower"]+=1
    
    print(f"{s}: ")
    print(f"No. majuscule: ",d["NbrUpper"])
    print(f"No. minuscule: ",d["NbrLower"])

my_string("Banque Centrale des Etats de l'Afrique de l'Ouest-BCEAO")
