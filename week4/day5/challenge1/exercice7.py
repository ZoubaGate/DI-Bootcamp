#exercice7
#Write a function that counts an element in a list (without using the count method):
def list_count(liste,letter):
    count=0
    for i in liste:
        if i == letter:
            count+=1
    print(count)
list_count(['a','a','t','o'],'a')