#Exercise 8 : How Old Are You On Jupiter?

'''
    Given an age in seconds, calculate how old someone would be on:
    Earth: orbital period 365.25 Earth days, or 31557600 seconds
    Mercury: orbital period 0.2408467 Earth years
    Venus: orbital period 0.61519726 Earth years
    Mars: orbital period 1.8808158 Earth years
    Jupiter: orbital period 11.862615 Earth years
    Saturn: orbital period 29.447498 Earth years
    Uranus: orbital period 84.016846 Earth years
    Neptune: orbital period 164.79132 Earth years
    So if you are told someone is 1,000,000,000
    seconds old, the function should output that
    they are 31.69 Earth-years old.
'''
age = int(input("give your age: "))
sAge = age*365.25*24*60*60
print(sAge)
print(f'''
        Earth: are {sAge/31557600} Earth-years old.
        Mercury: {sAge/31557600*0.2408467} Earth years
        Venus: {sAge/31557600*0.61519726} Earth years
        Mars: {sAge/31557600*1.8808158} Earth years
        Jupiter: {sAge/31557600*11.862615} Earth years
        Saturn: {sAge/31557600*29.447498} Earth years
        Uranus: {sAge/31557600*84.016846} Earth years
        Neptune: {sAge/31557600*164.79132} Earth years
      ''')