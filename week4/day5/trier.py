#Défi Quotidien : Trier
# Écrivez un programme qui accepte une séquence de mots séparés par des virgules en entrée
# et imprime les mots dans une séquence séparée par des virgules après les avoir triés par
# ordre alphabétique.
# Utiliser la compréhension de liste

ma_liste = []
while True:
    mot = input("entrer un mot ou taper \"q\" pour quitter: ")
    if mot == 'q': break
    ma_liste.append(mot)
print("Ma liste de mot saisie: ")
print(','.join(ma_liste))
print("Ma liste de mot saisie par ordre aphabetique: ")
print(','.join(sorted(ma_liste)))