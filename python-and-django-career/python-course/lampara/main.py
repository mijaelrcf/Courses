# Un módulo permite agrupar funcionalidad y ocultar la complejidad.
# Para poder requerir un módulo podemos utilizar import

from Lamp import Lamp

def run():
    lamp = Lamp(is_turned_on = False)

    while True:
        command = str(input('''
        que deseas hacer?
        [p]render
        [a]pagar
        [s]alir

        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            print('goodbye')
            break

if __name__ == "__main__":
    run()