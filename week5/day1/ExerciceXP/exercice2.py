#exercice2
class Dog:
    def __init__(self,name,height):
        self.name=name
        self.height = height
    
    def bark(self):
        print(f"{self.name} va woof!")
    def jump(self):
        x = self.height*2
        print(f"{self.name} jumps {x} cm high!")

davids_dog = Dog("Reg",50)
print(f"Name dog: {davids_dog.name}")
print(f"height dog: {davids_dog.height}")
davids_dog.bark()
davids_dog.jump()
        
print()
sarahs_dog = Dog("Teacup",20)
print(f"Name of sarah dog: {sarahs_dog.name} and height dog: {sarahs_dog.height}")
sarahs_dog.bark()
sarahs_dog.jump()
print()
if sarahs_dog.height > davids_dog.height:
    print("sarah dog is heighter than david dog")
else:
    print("david dog is heighter than sarah dog")