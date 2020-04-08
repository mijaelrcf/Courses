print('LIST COMPRENHENSION')
print('pares with for')
pares = []
for num in range(1, 31):
    if num % 2 == 0:
        pares.append(num)

print(pares)

print('pares with list comprenhension')
even = [num for num in range(1, 31) if num % 2 == 0]
print(even)


print('DICTIONARY COMPRENHENSION')
print('squares with for')
cuadrados = {}
for num in range(1, 11):
    cuadrados[num] = num**2

print(cuadrados)

print('squares with dictionary comprenhension')
squares = {num: num**2 for num in range(1, 11)}
print(squares)
