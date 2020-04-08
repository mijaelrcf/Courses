import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

def get_random_word():
    index = random.randint(0, len(WORDS) - 1)
    return WORDS[index]
    
def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print ('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- ')

def run():
    word = get_random_word()
    hidden_word = ['_'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('type one letter: '))

        letter_indexes = []
        for index in range(len(word)):
            if word[index] == current_letter:
                letter_indexes.append(index)

        if len(letter_indexes) == 0:
            tries += 1
            
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('¡Perdiste! La palabra correcta era {}'.format(word))
                break
        else:
            for index in letter_indexes:
                hidden_word[index] = current_letter

            letter_indexes =[]
        
        try:
            hidden_word.index('_')
        except ValueError:
            print('')
            print('¡Felicidades! Ganaste. La palabra es: {}'.format(word))
            break
    
if __name__ == "__main__":
    print('WELCOME TO THE HUNGED GAME')
    run()