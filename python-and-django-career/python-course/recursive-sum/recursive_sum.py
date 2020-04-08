
def sum(num):
    if(num == 1):
        return 1
    else:
        return num + sum(num - 1)


def run():
    num = int(input('Ingrese un número: '))
    for i in range(num):
        print('{} + '.format(i + 1)) 
    result = sum(num)
    print('El resultado es: {}'.format(result))

if __name__ == "__main__":    
    print('B I E N V E N I D O  A L  P R O G R A M A  D E  S U M A  R E C U R S I V A ')
    run()