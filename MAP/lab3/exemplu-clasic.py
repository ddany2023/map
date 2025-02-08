from tkinter import *

obiect = Tk()
obiect.title("Tipuri de persoane")
#obiect.geometry("420x560")
variabila_gen = StringVar(value="masculin")
varibila_tip = StringVar(value = "fumator")
#TIP
frame_tip_om = LabelFrame(obiect,text="Alegere")
frame_tip_om.pack(side="right")
Radiobutton(frame_tip_om,text="fumator", value="fumator",variable=varibila_tip).pack(anchor="w")
Radiobutton(frame_tip_om,text="NEfumator", value="nefumator", variable=varibila_tip).pack(anchor="w")
#GEN
frame_gen = LabelFrame(obiect,text="Gen").pack(side="left")
#frame_gen.pack(side="left")
Radiobutton(frame_gen,text="Masculin", value="masculin", variable=variabila_gen).pack(anchor="w")
Radiobutton(frame_gen,text="Feminin", value="feminin", variable=variabila_gen).pack(anchor="w")
label_rezultat = Label(obiect,text="TEST")
label_rezultat.pack(side="bottom")
def afla():
    global variabila_gen
    if variabila_gen.get()=="masculin":
        gen = "barbat"
        fumator = "fumator" if varibila_tip.get()=="fumator" else "nefumator"
    else:
        gen = "femeie"
        fumator = "fumatoare" if varibila_tip.get()=="fumator" else "nefumatoare"
    mesaj = f"Esti {gen} {fumator}"
    label_rezultat.config(text=mesaj)
buton_actiune = Button(obiect,text="Afla raspunsul", command=afla)
buton_actiune.pack()
mainloop()