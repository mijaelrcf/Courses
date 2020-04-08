import turtle

def main():
    window = turtle.Screen()    
    mija = turtle.Turtle()

    make_square(mija)

    turtle.mainloop()

def make_square(mija):
    length = int(input('length square: '))
    
    for i in range(4):
        make_line_and_turn(mija, length)
    

def make_line_and_turn(mija, length):
    mija.forward(length)
    mija.left(90)

if __name__ == '__main__':
    main()