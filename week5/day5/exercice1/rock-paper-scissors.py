#****************Rock-paper-scissors******************
from game import Game
myGame=Game()
def get_user_menu_choice():
    choice=input('''\tMenu: 
                (g) Play a new game
                (q) Show scores and exit
                 : 
                 ''')
    return choice

def print_results(results):
    print("\tGame Results: ")
    for k in results:
        print(f"\tYou {k} {results[k]} times")
    print("\tThank you for playing")

def main():
    while True:
        choice = get_user_menu_choice()
        match choice:
            case 'g':
                print(myGame.play())
            case 'q':
                print_results(myGame.dico)
                exit()

main()
    