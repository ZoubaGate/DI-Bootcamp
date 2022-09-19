# Exercise 5 : Let’s Create Some Personalized Shirts !

#1- Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
#2- The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
def make_shirt(taille="large", texte="l love python"):
    print("The size of the shirt is {} and the text is {}".format(taille,texte))
#3- Call the function make_shirt()
make_shirt()
#4- Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.

#5- Make a large shirt with the default message

#6- Make medium shirt with the default message
make_shirt("medium")
#7- Make a shirt of any size with a different message.
make_shirt("little","i love javaScript")

#8- Bonus: Call the function make_shirt() using keyword arguments.

make_shirt(taille="very little",texte="i love css")