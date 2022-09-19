#exercice2
#Draw the following pattern using for loops:
n=6
espace=" "
for i in range(0,n):
    print(espace*(n-i),"*"*i,end="")
    print()