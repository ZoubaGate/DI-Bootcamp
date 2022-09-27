from menu_manager import MenuManager

new = MenuManager()


def show_user_menu():
    while True:
        choose=input('''
            MENU
            (a) Add an item
            (d) Delete an item
            (v) View the menu
            (x) Exit
            : 
            ''')
        match choose:
            case "a":
                add_item_to_menu()
            
            case "d":
                remove_item_from_menu()
                
            case "v":
                show_restaurant_menu()
                
            case "x":
                show_restaurant_menu()
                new.save_to_file()
                exit()

def add_item_to_menu():
    name=input("give the item's name: ")
    price=input("give the item's price: ")
    new.add_item(name,price)
    print("item was added successfully")

def remove_item_from_menu():
    rm=input("input the name of the item you want to renove from the restaurant's menu: ")
    if(new.remove_item(rm)):
        print('delete was completed')
    else:
        print('error: the item not exists in the restaurant menu.')

def show_restaurant_menu():
    for item in new.menu['items']:
        print(item)
        
if __name__=='__main__':
    show_user_menu()