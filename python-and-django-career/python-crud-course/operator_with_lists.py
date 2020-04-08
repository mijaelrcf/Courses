# Operators with lists
a = list(range(0, 3))
b = list(range(3, 6))

print(a)
print(b)

print(a + b)
#a + b = [0, 1, 2, 3, 4, 5]

# append: añade al final
fruits = list()
print(fruits)

fruits.append('apple')
print(len(fruits))
fruits.append('banana')

fruits.append('kiwi')

print(fruits)

some_fruit = fruits.pop()
print(some_fruit)

some_fruit = fruits.pop(0)
print(some_fruit)

del fruits[0]

import random 

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(0, 15))

print(random_numbers)

# no modifica la lista inicial
ordered_numbers = sorted(random_numbers)
print(ordered_numbers)
print(random_numbers)

# si queremos ordenar la lista inicial utilizamos sort
random_numbers.sort()
print(ordered_numbers)

print(dir(random_numbers))

# pop: elimina el ultimo elemento de la lista
a.pop

# sort: ordena la lista
a.sort

# del: elimina elementos con indices
del a[-1]

# remove: elimina por el valor 

