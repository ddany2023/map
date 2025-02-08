from tkinter import *
from tkinter import messagebox
obiect = Tk()
obiect.geometry("350x350")
obiect.title("Primul meu proiect")
Label(obiect, text="Nume",font=('Arial',12)).grid(row=0)        #.place(x=200,y=50))
Label(obiect, text="Prenume", font=('Times New Roman',12),justify="left").grid(row=1)              #place(x=0,y=25)
nume = Entry(obiect)
nume.grid(row=0,column=1)
prenume = Entry(obiect)
prenume.grid(row=1, column=1)
def intampinare():
    name = nume.get()
    lastname = prenume.get()
    messagebox.showerror("Intampinare",f"Salut, {name} {lastname}")
Button(obiect, text="Salut",command=intampinare).grid(row=2)
mainloop()