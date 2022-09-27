#week5 
# Exercise 4 : Afternoon At The Zoo
class Zoo:
    def __init__(self,zoo_name):
        self.zoo_name= zoo_name
        self.animals= []
    
    def add_animal(self,new_animal):
        if not new_animal in self.animals:
            self.animals.append(new_animal)
    
    def get_animals(self):
        for i in self.animals:
            print(i,end=", ")
    
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    
    def sort_animals(self):
        dico = {}
        trier = sorted(self.animals)
        
        res=[]
        x=[]
        for i in trier:
            if i[0] not in x:
                x.append(i[0])
        for i in x:
            p=[]
            for j in trier:
                if j[0]==i:
                    p.append(j)
            res.append(p) 
        for k,v in enumerate(res):
            dico[k]=v
        print(dico)
        
ramat_gan_safari = Zoo("zogona")
x=""
while True:
    x=input("Which animal should we add to the zoo or write \"q\" to exit: ")
    if x == "q": break
    ramat_gan_safari.add_animal(x)
ramat_gan_safari.get_animals()
#y = input("\nwhat animal do you want to sell: ")
#ramat_gan_safari.sell_animal(y)
ramat_gan_safari.get_animals()
print()
ramat_gan_safari.sort_animals()


        