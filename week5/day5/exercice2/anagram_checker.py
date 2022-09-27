#*******************Anagramchecker************************
import re
from collections import *
import string
class AnagramChecker:
    def __init__(self):
        with open('sowpods.txt','r') as f:
            self.words = f.readlines()
            self.words = [i.replace('\n','').lower() for i in self.words ]
    
    def is_valid_word(self,word):
        word=word.lower().strip()
        return word.isalpha()
 
    def is_anagram(self,word1, word2):
        if (Counter(word1)==Counter(word2)):
            return True
        else:
            return False
    def get_anagrams(self,word):
        self.anag=[]
        for i in self.words:
             if self.is_anagram(word,i):
                 self.anag.append(i)
        print(self.anag)
    
if __name__=='__main__':
    x = AnagramChecker()
    #print(x.words)
    x.is_anagram('sidibe','diBesi')
    print(x.is_valid_word("sidibe")) 