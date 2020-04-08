# List comprehensions
lista_de_numeros = list(range(10))

print('lista de numeros')
print(lista_de_numeros)

pares = [numero for numero in lista_de_numeros if numero % 2 == 0]

print('pares')
print(pares)

# Dictionary comprehensions
student_uid = [1, 2, 3]
print('uids')
print(student_uid)

students = ['Juan', 'Jose', 'Larsen']
print('students')
print(students)

students_with_uid = {uid: student for uid, student in zip(student_uid, students)}

print('result')
print(students_with_uid)

# Sets comprehensions
import random
random_numbers = []

for i in range(10): 
    random_numbers.append(random.randint(1, 3))

print('random numbers')
print(random_numbers)

non_repeated = { number for number in random_numbers }
print('non repeated')
print(non_repeated)