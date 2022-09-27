#Exercise 2: Currencies
class Currency:
    #init methode
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    #code dunder string 
    def __str__(self):
      return f"{self.amount}  {self.currency}"
  
    #code dunder int
    def __int__(self):
        return self.amount.__int__()
    
    #code dunder repr
    def __repr__(self):
        return f"{self.amount} {self.currency}"
    
    #code dunder pour additionner les amount de 02 objets
    def __add__(self,object2):
        if type(object2)==int:
            return Currency(self.currency,self.amount+object2)
        else:
            if self.currency==object2.currency:
                return  Currency(self.currency,self.amount+object2.amount)
            else:
                return f'\t{self.currency} != {object2.currency}'

    
    
    
    
    
    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
print("________________afficher________________")
print("\tafficher c1 avec str: ",str(c1))
print("\tmontant de c1: ",int(c1))
print("\tafficher c1 avec repr: ",repr(c1))
print("\tadd c1.mount with 5: ",c1+5)
print("\tdo c1+c2: ",c1+c2)
print("\ton peut afficher c1 sans mettre repr et str\n\t dans le print\n\t car ils deja definie dans la classe: ",c1)
c1+=5
print("\tc1+=5 =>",c1)
c1+=c2
print("\tc1+=c2 =>",c1)
print(c1+c3)
