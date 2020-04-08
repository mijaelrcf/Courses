
KEYS = {
    'A': '01000001',
    'Á': '11000001',
    'B': '01000010',
    'C': '01000011',
    'D': '01000100',
    'E': '01000101',
    'É': '11001001',
    'F': '01000110',
    'G': '01000111',
    'H': '01001000',
    'I': '01001001',
    'Í': '11001101',
    'J': '01001010',
    'K': '01001011',
    'L': '01001100',
    'M': '01001101',
    'N': '01001110',
    'Ñ': '11010001',
    'O': '01001111',
    'Ó': '11010011',
    'P': '01010000',
    'Q': '01010001',
    'R': '01010010',
    'S': '01010011',
    'T': '01010100',
    'U': '01010101',
    'Ú': '11011010',
    'Ü': '11011100',
    'V': '01010110',
    'W': '01010111',
    'X': '01011000',
    'Y': '01011001',
    'Z': '01011010',
    'a': '01100001',
    'á': '11100001',
    'b': '01100010',
    'c': '01100011',
    'd': '01100100',
    'e': '01100101',
    'é': '11101001',
    'f': '01100110',
    'g': '01100111',
    'h': '01101000',
    'i': '01101001',
    'í': '11101101',
    'j': '01101010',
    'k': '01101011',
    'l': '01101100',
    'm': '01101101',
    'n': '01101110',
    'ñ': '11110001',
    'o': '01101111',
    'ó': '11110011',
    'p': '01110000',
    'q': '01110001',
    'r': '01110010',
    's': '01110011',
    't': '01110100',
    'u': '01110101',
    'ú': '11111010',
    'ü': '11111100',
    'v': '01110110',
    'w': '01110111',
    'x': '01111000',
    'y': '01111001',
    'z': '01111010',
    ',': '00101100',
    '?': '00111111',
    '!': '00100001',
}

def cypher(message):
    words = message.split(' ')
    cypher_message = []

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)

    return ' '.join(cypher_message)

def decipher(message):
    print(message)
    words = message.split(' ')
    print(words)
    decipher_message = []

    for word in words:
        decipher_word = ''
        n = 8
        word = [word[i:i+n] for i in range(0, len(word), n)]
        for letter in word:
            for key, value in KEYS.items():
                if value == letter:
                    decipher_word += key

        decipher_message.append(decipher_word)

    return ' '.join(decipher_message)

def run():

    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. 

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
            
            ¿Qué deseas hacer?
            Ingrese una opcion: '''))

        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(input('Escribe tu mensaje cifrado: '))
            decypher_message = decipher(message)
            print(decypher_message)
        elif command == 's':
            print('bye')
            exit()
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S   C I F R A D O S')
    run()