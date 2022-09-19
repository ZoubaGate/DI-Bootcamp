#Exercise 4 : Disney Characters
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
number = [0,1,2,3,4,]

disney_users_A = dict(zip(users,number))
print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

disney_users_B = dict(zip(number,users))
print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
print("\n")
users = sorted(users)
disney_users_C = dict(zip(users,number))
print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

# Only recreate the 1st result for:
print("\nThe characters, which names contain the letter “i”: ")
for name in disney_users_A:
    if 'i' in name:
        print(name)

print("\n")
print("The characters, which names start with the letter “m” or “p”: ")
for name in disney_users_A:
    if name[0].lower() == 'm' or name[0].lower()=='p':
        print(name)
        
