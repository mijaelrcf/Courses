class Car:
    _CARS = ['''
      ______
     /|_||_\`.__
    (   _    _ _'\'
    =`-(_)--(_)-' 
    ''',
    '''
              *  *  *
      ______   \ | /
     /|_||_\`.__ *
    (   _    _ _\ 
    =`-(_)--(_)-' 
    ''',
    '''
          ______
         /|_||_\`.__
    *** (   _    _ _\ --->
    *** =`-(_)--(_)-' --->
    ''']

    def __init__(self, is_turned_on, is_move):
        self._is_turned_on = is_turned_on  
        self._is_move = is_move      

    def turn_off(self):
        self._is_turned_on = False
        print(self._CARS[0])

    def turn_on(self):
        self._is_turned_on = True
        print(self._CARS[1])
    
    def move(self):
        self._is_move = True
        print(self._CARS[2])

    

def run():
    car = Car(is_turned_on = False, is_move = False)

    while True:
        command = str(input('''
        CAR OPTIONS:
            [of]f
            [o]n
            [m]ove            
            [q]uit
        
        type an option please: '''))

        if command == 'o':
            car.turn_on()
        elif command == 'm':
            car.move()
        elif command == 'of':
            car.turn_off()
        else:
            print('goodbye')
            break

if __name__ == "__main__":
    print('W E L C O M E  T O  C A R  C L A S S')
    run()