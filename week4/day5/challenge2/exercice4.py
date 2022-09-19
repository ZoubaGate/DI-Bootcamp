my_list = [2, 24, 12, 354, 233]  #liste
for i in range(len(my_list) - 1):  #parcourir les element de la liste -1
    minimum = i  #supposition d'un element plus petit
    for j in range( i + 1, len(my_list)): #parcourir les element de la liste a partir d'element supposer minimun  choisie
        if(my_list[j] < my_list[minimum]): #verifier si un element de la liste est plus petit que l'element supposer choisi
            minimum = j #si c'est le cas,on renisialise notre variable avec le nouveau indice
            if(minimum != i): # s
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)