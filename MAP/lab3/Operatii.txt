from tkinter import *
from tkinter import messagebox

obiect = Tk()
obiect.title("Calculator SIMPLU")
val_1_Label = Label(obiect, text="First value:")
val_1_Label.grid(row=0)
val1 = Entry(obiect)
val1.grid(row=1,column=0)

val_2_Label = Label(obiect, text="Second value:")
val_2_Label.grid(row=2)
val2 = Entry(obiect)
val2.grid(row=3,column=0)
label_rezultat = Label(obiect,text="")
label_rezultat.grid(row=1, column=1)
def adunare():
    try:
        valoare1 = float(val1.get())
        valoare2 = float(val2.get())
        print(valoare1,valoare2)
        rezultat = valoare1 + valoare2
        label_rezultat.config(text=f"Rezultat: {rezultat}")
    except:
        messagebox.showerror("Error", "Introdu valori valide!")

def scadere():
    try:
        valoare1 = float(val1.get())
        valoare2 = float(val2.get())
        print(valoare1,valoare2)
        rezultat = valoare1 - valoare2
        label_rezultat.config(text=f"Rezultat: {rezultat}")
    except:
        messagebox.showerror("Error", "Introdu valori valide!")

def inmultire():
    try:
        valoare1 = float(val1.get())
        valoare2 = float(val2.get())
        print(valoare1,valoare2)
        rezultat = valoare1 * valoare2
        label_rezultat.config(text=f"Rezultat: {rezultat}")
    except:
        messagebox.showerror("Error", "Introdu valori valide!")

def impartire():
    try:
        valoare1 = float(val1.get())
        valoare2 = float(val2.get())
        if valoare2 == 0:
            messagebox.error("Error","Nu se poate face impartirea! ")
        rezultat = valoare1 / valoare2
        label_rezultat.config(text=f"Rezultat: {rezultat}")
    except:
        messagebox.showerror("Error", "Introdu valori valide!")

def stergere():
    val1.delete(0,END)
    val2.delete(0,END)
    label_rezultat.config(text="")

Button(obiect, text = "+", width=10,padx=10,bg="blue", command=adunare).grid(row=4,column=0, sticky="w")
Button(obiect, text = "-", width=10,padx=10,bg="blue", command=scadere).grid(row=4,column=1)
Button(obiect, text = "*", width=10,padx=10,bg="blue", command=inmultire).grid(row=5,column=0)
Button(obiect, text = "/", width=10,padx=10,bg="blue", command=impartire).grid(row=5,column=1)
Button(obiect, text="C", width=10,padx=10,bg="blue", command=stergere).grid(row=6,column=0, columnspan=2)
mainloop()