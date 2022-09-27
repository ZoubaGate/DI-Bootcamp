#Daily Challenge: Translator
'''
from translate import Translator
translator= Translator(to_lang="eng")


french_words= ["Bonjour", "revoir", "Bienvenue", "bientôt"] 


english_words = {}
for word in french_words:
    x=translator.translate(word)
    english_words[word]=x
print(english_words)

'''
french_words= ["Bonjour", "revoir", "Bienvenue", "bientôt"] 
english_words = ["Hello","Goodbye","Welcome","See you soon"]
translate={}
for i in range(len(french_words)):
    translate[french_words[i]]=english_words[i]
print(translate)
