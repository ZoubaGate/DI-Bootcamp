#***********************anagrams*********************************
from anagram_checker import AnagramChecker

myAnagram = AnagramChecker()
def menu():
    while True:
        valid = input('''
                     ***Menu***
                     (w) input a word
                     (q) exit
                     : ''')
        match valid:
            case 'q':
                exit()
            case 'w':
                word = input('input a single word,only alphabetics caracter: ')
                if(myAnagram.is_valid_word(word)):
                    print(f"YOUR WORD : {word}")
                    print("this is a valid English word.")
                    print("Anagrams for your word: ",end="")
                    myAnagram.get_anagrams(word)
                else:
                    print("your word is no correct!")

menu()
        