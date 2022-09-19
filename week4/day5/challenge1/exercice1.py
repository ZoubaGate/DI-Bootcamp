#Write a script that inserts an item at a defined index in a list.
liste = ["moi","lui","elle","leur"]
position = int(input("position: "))
valeur = input("valeur: ")
liste.insert(position,valeur)
for k,v in enumerate(liste):
    print(k, " => ",v)
