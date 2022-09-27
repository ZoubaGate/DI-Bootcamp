#Exercise 6 : Birthday And Minutes
from datetime import *
''' Create a function that accepts a birthdate
    as an argument (in the format of your choice),
    then displays a message stating how many minutes
    the user lived in his life.
'''
def birthdate(born):
    today = datetime.now(
        
    )
    x = (today-born)
    mn = (x.days*24*60)    
    print("you lived {} in his life".format(mn))

birthdate(datetime(2000,6,7,12,32,40,1000))