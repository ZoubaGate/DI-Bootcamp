#**********game**************
import random
class Game:
    def __init__(self):
        self.dico = {
            'win': 0,
            'loss': 0,
            'draw': 0
        }
    def get_user_item(self):
        user_item=""
        while user_item!='r' and user_item!='p' and user_item!='s':
            user_item = input("Select (r)ock, (p)aper, or (s)cissors: ")
        return user_item
    
    def get_computer_item(self):
        computer_item = random.choice(['r','p','s'])
        return computer_item
    
    def get_game_result(self,user_item,computer_item):
        if user_item==computer_item:
            self.dico['draw']+=1
            return f"draw"
       
        if user_item=='r' and computer_item=='s':
            self.dico['win']+=1
            return f"win"
        elif user_item=='s' and computer_item=='p':
            self.dico['win']+=1
            return f'win'
        elif user_item=='p' and computer_item=='r':
            self.dico['win']+=1
            return f'win'
        else:
            self.dico['loss']+=1
            return f'loss'
            
    
    def play(self):
        dico = {
            'p': 'paper',
            'r': 'rock',
            's':'scissors'
        }
        results= {}
        user_item=self.get_user_item()
        computer_item = self.get_computer_item()
        game=self.get_game_result(user_item,computer_item)
        return f"You selected {dico[user_item]}. The computer selected {dico[computer_item]}. You {game}"
    
