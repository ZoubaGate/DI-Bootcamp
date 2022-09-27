#Exercise 5 : Amount Of Time Left Until January 1st
from datetime import *
''' Create a function that displays the
    amount of time left from now until January 1st.
    (Example: the 1st of January is in 10 days and
    10:34:01hours).
'''
a = "2023/01/01"
dt = datetime.strptime(a,"%Y/%m/%d")
to=datetime.now()

print()


print("the 1st of January is in {}".format(dt-to))

