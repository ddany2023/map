import turtle

def hilbert_curve(t, order, size, direction=1):
   # Funcție recursivă pentru desenarea curbei lui Hilbert.
    if order == 0:
        return

    # Rotire inițială
    t.left(direction * 90)
    hilbert_curve(t, order - 1, size, -direction)

    # Pas înainte
    t.forward(size)
    t.right(direction * 90)
    hilbert_curve(t, order - 1, size, direction)

    # Pas înainte
    t.forward(size)
    hilbert_curve(t, order - 1, size, direction)

    # Rotire finală
    t.right(direction * 90)
    t.forward(size)
    hilbert_curve(t, order - 1, size, -direction)
    t.left(direction * 90)

def main():
    # Citirea ordinului curbei de la utilizator
    try:
        order = int(input("Introduceți ordinul curbei lui Hilbert (de exemplu, 2 sau 3): "))
    except ValueError:
        print("Vă rugăm să introduceți un număr întreg valid!")
        return

    # Configurarea ecranului Turtle
    screen = turtle.Screen()
    screen.title("Curba lui Hilbert")
    t = turtle.Turtle()
    t.speed("slowest")  # Setare la viteza maximă

    # Dimensiunea pasului în funcție de ordin
    size = 200 // (2 ** order)
    
    # Recentrăm desenul
    t.penup()
    t.goto(-200 // 2, 200 // 2)
    t.pendown()

    # Desenăm curba lui Hilbert
    hilbert_curve(t, order, size)

    # Finalizare
    turtle.done()

if __name__ == "__main__":
    main()
