class Human:
    def __init__(self,id_number,name,age,priority,blood_type):
        self.id_number=id_number
        self.name=name
        self.age=age
        self.priority=priority
        self.blood_type=blood_type
        self.family=[]

    def add_family_member(self, person):
        self.family.append(person)
        
        
        
class Queue(Human):
    def __init__(self):
        self.humans=[]
    
    def display(self):
        for i in self.humans:
            # print(i.id_number)
            # print(i.name)
            # print(i.age)
            # print(i.priority)
            # print(i.blood_type)
            print(i.name)
            
    def get_next(self):
        personTake = self.humans[0]
        #del self.humans[0]
        print(self.humans[0].id_number)
        print(self.humans[0].name)
        print(self.humans[0].age)
        print(self.humans[0].priority)
        print(self.humans[0].blood_type)
    
    def add_person(self, person):
        if person.age>=60 or person.priority==True:
            self.humans=[person,*self.humans]
        else:
            self.humans.append(person)
        
    
    def find_in_queue(self,person):
        for pers in self.humans:
            if pers.id_number == person.id_number:
                return self.humans.index(person)
        
    def swap(self, person1, person2):
        self.humans[person1],self.humans[person2] =  self.humans[person2],self.humans[person1]
        return self.humans
    
    
    
    def get_next_blood_type(self, blood_type):
        for person in self.humans:
            if person.blood_type == blood_type:
                personTake = person
                del self.humans[person]
                return personTake
    
    def sort_by_age(self):
        for person1 in self.humans:
            for person2 in self.humans:
                if person1.age>person2.age:
                    swap(person1,person2)
        priority=[]
        older=[]
        younger=[]
        for person in self.humans:
            if person.priority==True:
                priority.append(person)
            if person.age>=60:
                older.append(person)
            younger.append(person)
        sortList=priority+older+younger
        return sortList
        
   


if __name__=='__main__':
    file = Queue()
    person2 = Human(2,'sanou',24,False,'A')
    person3 = Human(3,'bado',12,True,'B')
    
    
    file.add_person(person2)
    file.add_person(person3)
    file.display()
    
   