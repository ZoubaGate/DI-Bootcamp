#Exercice 3 : Zara
brand = {
    'name': "Zara",
    'creation_date': 1975,
    'creator_name': "Amancio Ortega Gaona",
    'type_of_clothes': ['men', 'women', 'children', 'home'], 
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': "blue", 
        'Spain': "red", 
        'US': ['pink', 'green']
    }
    
}
brand['number_stores']=2

#4-Print a sentence that explains who Zaras clients are.
#5-Add a key called country_creation with a value of Spain.
brand["country_creation"]="spain"

    
#6-Check if the key international_competitors is in the dictionary
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
print(brand['international_competitors'])

#7-Delete the information about the date of creation.
del brand['creation_date']


#8-Print the last international competitor.
print("the last international competitor",brand['international_competitors'][-1])



#9-Print the major clothes colors in the US.
print("\nPrint the major clothes colors in the US")
for i in brand['major_color']['US']:
    print(i)
    
#10- Print the amount of key value pairs:
print("\nPrint the amount of key value pairs: ")
print(len(brand))

#11- Print the keys of the dictionary.
print("\nPrint the keys of the dictionary:")
for i in brand:
    print(i)

#12-Create another dictionary called more_on_zara with the following details
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

#13-Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)
for key,value in brand.items():
    print(key,"=>",value)
    
print(brand['number_stores'])

#Ca s'affiche 
