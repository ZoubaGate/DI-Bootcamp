#Write a script that counts the number of spaces in a string.
my_string = "si di be zou ba ir "
spaceCount = 0
for v in my_string:
    if v == " ":
        spaceCount+=1
print(f"{my_string} contient {spaceCount} espaces")
