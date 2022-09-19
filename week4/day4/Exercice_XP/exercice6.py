# Exercice 6 : Magiciens …

#1- En utilisant cette liste de noms de magiciens.magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
#2-Passez la liste à une fonction appelée show_magicians(), qui imprime le nom de chaque magicien de la liste.
def show_magicians(liste):
    for item in liste:
        print(item)
#show_magicians(magician_names)
'''3-Écrivez une fonction appelée make_great()qui modifie la liste des magiciens en ajoutant la phrase "the Great"au nom de chaque magicien.'''
def make_great(names,names2):
    while names:
        name = "the great "+names.pop()
        names2.append(name)
names2=[]
make_great(magician_names,names2)
show_magicians(names2)

#4-Appelez la fonction make_great()
#50Appelez la fonction show_magicians()pour voir que la liste a bien été modifiée.