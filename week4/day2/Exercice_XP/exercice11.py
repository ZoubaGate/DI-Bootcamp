#Exercise 11 : Sandwich Orders#2

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

print("the deli has run out of pastrami")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    
print(sandwich_orders)

