#Exercise 9 : Faker Module
from faker import Faker
sample = Faker()
users=[]

def adds(newDict):
    users.append(newDict)
for i in range(10):
    new = {
    "name": sample.name(),
    "adress": sample.address(),
    "langage_code": sample.language_code()
    }
    adds(new)

for i in users:
    print(i)
    
