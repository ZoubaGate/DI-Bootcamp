#Exercise 3: String Module
import random
import string
'''
    Generate random String of length 5
'''
N = 5
#using random.choices()
#generating random strings

res = ''.join(random.choices(string.ascii_letters,k=N))

#print result
print("the generated random string: "+str(res))

