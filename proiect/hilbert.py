import turtle

def hilbert_curve(t, order, size, direction=1):
    if order == 0:
        return

    t.left(direction * 90)
    hilbert_curve(t, order - 1, size, -direction)

    t.forward(size)
    t.right(direction * 90)
    hilbert_curve(t, order - 1, size, direction)

    t.forward(size)
    hilbert_curve(t, order - 1, size, direction)

    t.right(direction * 90)
    t.forward(size)
    hilbert_curve(t, order - 1, size, -direction)
    t.left(direction * 90)

def main():
    try:
        order = int(input("Introduceți ordinul curbei lui Hilbert: "))
    except ValueError:
        print("Vă rugăm să introduceți un număr întreg valid!")
        return

    screen = turtle.Screen()
    screen.title("Curba lui Hilbert")
    t = turtle.Turtle()
    t.speed("fastest")

    size = 200 // (2 ** order)
    
    t.penup()
    t.goto(-200 // 2, 100 // 2)
    t.pendown()

    hilbert_curve(t, order, size)

    turtle.done()

if __name__ == "__main__":
    main()
