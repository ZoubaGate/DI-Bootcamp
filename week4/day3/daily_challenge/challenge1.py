#challenge 1
word = input("input a word please: ")
dic = {}
for i,letter in enumerate(word):
        if letter not in dic:
            dic[letter] = []
        dic[letter].append(i)
print(dic)