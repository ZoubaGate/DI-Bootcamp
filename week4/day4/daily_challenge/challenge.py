import re
# Daily Challenge: Solve The Matrix

'''
To decrypt the matrix,
Neo reads each column from 
top to bottom, starting from
the leftmost column, selecting
only the alpha characters and
connecting them.
Then he replaces every group
of symbols between two alpha
characters by a space.
'''

m=[
    [7,'i',3],
    ['T','s','i'],
    ['h','%','x'],
    ['i',' ', '#'],
    ['s','M',' '],
    ['$','a',' '],
    ['#','t','%'],
    ['^','r','!']
]
m2= list(zip(*m))
r=len(m2)
c=len(m2[0])
#print(m2)
l=[]
for i in range(r):
    char=0
    for j in range(c):
        char=m2[i][j]
        if type(char)==int:
            continue
        else:
            l.append(char)
l = "".join(l)
print(re.sub('(?<=[a-zA-Z])+[^a-zA-Z]+(?=[a-zA-Z])',' ',l))
