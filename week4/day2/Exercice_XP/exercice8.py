#Exercise 8: Who Ordered A Pizza ?
listPizza = []
value=''

while True:
    value=input("enter the name of pizza: ")
    listPizza.append(value)
    reponse=input("you'll add that topping to their pizza: ")
    if reponse=='oui':
        continue
    else:
        break
#calculate the total price of the pizza:
totalPrice = (10+2.5)*len(listPizza)
    
print("the all toppings on the pizza pie is ",listPizza," and the total price is: ",totalPrice)

