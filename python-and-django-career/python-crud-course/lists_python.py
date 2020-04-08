countries = ['Mexico','Venezuela','Colombia']

recipe = ['Ensalada', 3, 'lechugas', 2]

global_countries = countries

print(countries)
print(global_countries)

countries[0] = 'Guatemala'

print(countries)
print(global_countries)

import copy
countries = ['Mexico','Venezuela','Colombia']

global_countries = None
global_countries = copy.copy(countries)

print(countries)
print(global_countries)

countries[0] = 'Honduras'

print(countries)
print(global_countries)

for country in countries:
    print(country)

