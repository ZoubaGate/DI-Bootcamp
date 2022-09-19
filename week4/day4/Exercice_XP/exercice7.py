import random
#Exercice 7 : Conseils De Température
#1. Créez une fonction appelée get_random_temp().
#1.1 Cette fonction doit renvoyer un entier entre -10 et 40 degrés (Celsius), sélectionné au hasard.
def get_random_temp():
       return random.randint(-10,40)
#1.2 Testez votre fonction pour vous assurer qu'elle génère les résultats attendus.
print(get_random_temp())

#2- Créez une fonction appelée main()
# 2-1Dans cette fonction, appelez get_random_temp()pour obtenir une température et stockez sa valeur dans une variable.
def main():
    temp = get_random_temp()
# 2-2Informez l'utilisateur de la température dans un message amical, par ex. "La température actuelle est de 32 degrés Celsius."
    print("La température actuelle est de {} degrés Celsius".format(temp))

#3- Ajoutons plus de fonctionnalités à la main()fonction. Écrivez quelques conseils amicaux concernant la température :
# en dessous de zéro (par exemple "Brrr, c'est glacial ! Portez des couches supplémentaires aujourd'hui")
# entre zéro et 16 (ex. "Assez froid ! N'oubliez pas votre manteau")
# entre 16 et 23
# entre 24 et 32
# entre 32 et 40
def main():
    temp = get_random_temp()
    if temp < 0:
        print("Brrr, c'est glacial ! Portez des couches supplémentaires aujourd'hui")
    elif 0 < temp < 16:
        print("Assez froid ! N'oubliez pas votre manteau")
    elif 16 < temp < 23:
        print("un peu froid, n'oubliez pas votre pull")
    elif 24 < temp <32:
        print("il fait chaud, il faut sortir en blanc")
    else:
        print("il fait tres chaud, il faut sortir en t-shirt blanc")

#4- Modifiez la get_random_temp() fonction :
#4-1.)Ajoutez un paramètre à la fonction, nommé 'saison'.
#4-2.) À l'intérieur de la fonction, au lieu de simplement générer un nombre aléatoire entre -10 et 40, définissez des limites inférieures et supérieures en fonction de la saison, par exemple. si la saison est 'hiver', les températures ne devraient tomber qu'entre -10 et 16.
def get_random_temp(saison):
    if saison=="hiver":
        return random.randint(-10,16)
    elif saision=="automne":
        return random.randint(16,23)
    elif saison=="printemps":
        return random.randint(23,32)
    else:
        return random.randint(32,40)
        
#4-3.) Maintenant que nous avons changé get_random_temp(), changeons la main()fonction :
def main():
    saison = input("dans quels saisons etes vous: ")
    temp = get_random_temp(saision)
    
# Avant d'appeler get_random_temp(), nous devrons décider d'une saison, afin que nous puissions appeler la fonction correctement. Demandez à l'utilisateur de saisir une saison : "été", "automne" (vous pouvez utiliser "automne" si vous préférez), "hiver" ou "printemps".
# Utilisez la saison comme argument lors de l'appel get_random_temp().

# Bonus : Donnez la température sous forme de nombre à virgule flottante au lieu d'un entier.
# Bonus : Au lieu de demander la saison, demandez à l'utilisateur le numéro du mois (1 = janvier, 12 = décembre). Déterminez la saison en fonction du mois.

    