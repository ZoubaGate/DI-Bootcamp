# Créez un programme qui imprime une liste des articles que vous pouvez acheter dans le magasin avec l'argent que vous avez dans votre portefeuille.
# Triez la liste par ordre alphabétique.
# Renvoyez "Rien" si vous ne pouvez rien acheter du magasin.


items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1000",
  "Fertilizer": "$20"
}
list_product = []
wallet = "$300"
for k,v in items_purchase.items():
    if int(v[1:])<=int(wallet[1:]):
        list_product.append(k)
    else:
        list_product.append("NoThing")
print(list_product)
        

items_purchase2 = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet2 = "$1" 

list_product2 = []
wallet2 = "$300"
for k,v in items_purchase2.items():
    if int(v[1:])<=int(wallet2[1:]):
        list_product2.append(k)
    else:
        list_product2.append("NoThing")
print(list_product2)