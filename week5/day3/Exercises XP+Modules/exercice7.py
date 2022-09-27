#Exercise 7 : Upcoming Holiday
from datetime import *
'''
    Write a function that displays today’s date.
    The function should also display the amount of
    time left from now until the next upcoming holiday
    and print which holiday that is. (Example: the next
    holiday is in 30 days and 12:03:45 hours).
    Hint: Start by hardcoding the datetime and name of the upcoming holiday.
'''
def dt():
    td=datetime.now()
    holidays = datetime(2022,10,25,11,2,12)
    print("he next holiday is in ",holidays-td,"hours")
dt()
