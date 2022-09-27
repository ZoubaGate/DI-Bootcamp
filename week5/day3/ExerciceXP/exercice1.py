# Exercise 1 : Built-In Functions
class Exercise:
    
    def __init__(self,nombre):
        self.nombre = nombre
    def __abs__(self):
        return self.nombre.replace(self.nombre[0],"")
    def __int__(self):
        return int(self.nombre)
    def __input__(self):
        input("write some thing: ")
        return
    def __doc__(self):
        return '''   this is the documentation of my code:
                __init__ is used to initialise my class
                __abs__ return the absolute valeur of nombre
                __int__ return the nombre cinvert to int
                __input__ help as to input a vlaue in my object
        ''' 
myObject = Exercise("-10")
print(abs(myObject))
print(type(myObject.__int__()))
#print(myObject.__input__())
print(myObject.__doc__())

    
    
        