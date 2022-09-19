#Exercise 2 : Cinemax

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

#How much does each family member have to pay ?
totalCost=0
for member,age in family.items():
    if age < 3:
        print("the ticket is free for {}".format(member))
    elif 3<= age <= 12 :
        print("the ticket is $10 for {}".format(member))
        totalCost+=10
    else:
        print("the ticket is $15 for {}".format(member))
        totalCost+=15
#Print out the family’s total cost for the movies.
print("the family’s total cost for the movies is {}".format(totalCost))

#Bonus: 
newFamily = {}
answer = 'y'
while answer == 'y':
    name = input("input your name: ")
    newFamily[name] = int(input("input your age: "))
    answer = input("enter more name? ").lower()
print(newFamily)
