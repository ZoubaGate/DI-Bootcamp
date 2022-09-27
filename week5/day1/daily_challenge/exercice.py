#Daily Challenge: Old MacDonald’s Farm
class Farm:
    def __init__(self,name_farm):
        self.name_farm=name_farm
        self.animals= {}
    
    def add_animal(self,new_animal,number=1):
        if new_animal not in self.animals:
            self.animals[new_animal]=number
        else:
            self.animals[new_animal]+=number
        
    def get_info(self):
        print(f"Name farm: {self.name_farm}")
        for v in self.animals:
            print(v," : ",self.animals[v])
        print("\n\tE-I-E-I-0!")
    def get_animal_types(self):
        animeaux_trier = sorted(self.animals.keys())
        return animeaux_trier
    def get_short_info(self):
        animeaux =  self.get_animal_types()
        print("McDonald's possède: ",end="")
        for i in animeaux:
            if animeaux[-1]==i:
                print(f" et des {i}s",end=" ")
                break
            print(f"des {i}s",end=" ")
macdonald = Farm("McDonald")
macdonald.add_animal("lion")
macdonald.add_animal("lion")
macdonald.add_animal("lion")
macdonald.add_animal("chat",3)
macdonald.add_animal("mouton",12)
macdonald.get_info()
print(macdonald.get_animal_types())
macdonald.get_short_info()
