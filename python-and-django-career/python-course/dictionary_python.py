
calificaciones = dict()
calificaciones

calificaciones['algoritmos'] = 9
calificaciones['matematicas'] = 10
calificaciones['web'] = 8
calificaciones['bases_de_datos'] = 10
calificaciones

for key in calificaciones:
    print(key)

for value in calificaciones.values():
    print(value)

for key, value in calificaciones.items():
    print('llave: {}, valor: {}'.format(key, value))

