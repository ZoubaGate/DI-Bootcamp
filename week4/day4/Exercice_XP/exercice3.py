#Exercise 3 : Some Geography
# 1.)Write a function called describe_city() that accepts the name of a city and its country as parameters.
# 2.)The function should print a simple sentence, such as "<city> is in <country>".
# 3.)For example “Reykjavik is in Iceland”
# 4.)Give the country parameter a default value.
# 5.)Call your function.

def describe_city(nameCity,country="Burkina Faso"):
    print("{} is in {}".format(nameCity,country))
describe_city("bobo")

    