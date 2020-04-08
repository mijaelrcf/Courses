
def run():
    with open('numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))

def run2():
    counter = 0
    with open('aleph.txt') as f:
        for line in f:
            counter += line.count('Beatriz')
    
    print('Beatriz se encuentra {} veces en el texto'.format(counter))


if __name__ == "__main__":
    run2()