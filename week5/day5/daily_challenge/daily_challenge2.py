'''

'''

#Part 2: Create A Deck Of Cards Class.
import itertools
import random
class Card:
    def __init__(self,value,color):
        self.value=value
        self.color=color
colors = ['heart', 'diamonds', 'spades', 'clubs']
value=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
#deck = [Card(value, colors) for value in range(1, 14) for color in colors]
deck = list(itertools.product(value, colors))
random.shuffle(deck)
print(deck)
class Deck:
    def __init__():
        pass
    
    