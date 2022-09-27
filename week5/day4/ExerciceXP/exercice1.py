#Exercise 1 – Random Sentence Generator
import numpy
def get_words_from_file():
    global liste
    with open('sowpods.txt','r') as f:
        liste = f.readlines()
        liste = [el.replace('\n','') for el in liste]
def get_random_sentence(length): 
    word = numpy.random.choice(liste,length)
    word = ' '.join(word).lower()
    print(word)

if __name__=='__main__':
    x=int(0)
    print('''This function should read the file’s content and return the words as a collection
          ''')
    get_words_from_file()
    while x<2 or x>20:
        x=int(input(" how long you want the sentence to be,the values is in 2 and 20: "))    
    print("the words is: ")
    get_random_sentence(x)