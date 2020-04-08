
rae = {}
rae['pizza'] = 'La comida mas deliciosa del mundo'
print(rae)
rae['pasta'] = 'La comida mas sabrosa de Italia'
print(rae)

print(rae['pizza'])
print(rae['pasta'])

#
#print(rae['helado']) # genera un error 

# para no tener error se puede usar get
rae.get('helado', None)
a = rae.get('helado', None)
print(a)

a = rae.get('pizza', None)
print(a)

print(rae.keys())

print(rae.values())

print(rae.items())

for key in rae.keys():
    print(key)

for value in rae.values():
    print(value)

for key, value in rae.items():
    print(key, value)

print(dir(rae))

