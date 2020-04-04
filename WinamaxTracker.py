### REMERCIEMENT : SERTAMPS09 ###
from tkinter import *
from tkinter.ttk import *
from tkcalendar import *
from datetime import date

# setup
window = Tk()
window.title('Winamax Tracker - By Arclight & WB-44')
window.geometry('450x550')
window.resizable(0, 0)
window.iconbitmap("icon.ico")

# frames
frame=[Frame(window),Frame(window),Frame(window),Frame(window),Frame(window),Frame(window),Frame(window),Frame(window)]

# variable
data_nbjoueur = [9,10,5000,10000]
data_speed = ['Turbo', 'Normal']
data_typemdj = ['Sit and Go', 'Tournoi', 'Double or Nothing', 'Kill the Fish']
txt_var_variante=['NLHE', 'PLO', 'OTHER']
var_variante=[IntVar(), IntVar(), IntVar()]
var_speed=[]
resultatmdj=StringVar()
resultatmdj.set(1)
element2,element3=[],[]

def action_button():
    nbjoueur,mdj,speed,variante = cb_nbjoueur.get(),[],[],[]
    periode=[debut.get_date(),fin.get_date()]
    for k in range(len(txt_var_variante)): variante.append(var_variante[k].get())
    mdj = resultatmdj.get()
    for k in range(len(var_speed)): speed.append(var_speed[k].get())
    print(variante,nbjoueur,mdj,speed,periode)

def aff_frame(n) :
    if n>0 and n<(len(frame)-1) :
        sep = Separator(window, orient="horizontal")
        sep.pack(pady=8, fill=X)
    frame[n].pack()
    if n== (len(frame)-1):window.mainloop()

#1- variante
n=0
label_variante = Label(frame[n], text='Choix variante', font=("Arial", 11))
label_variante.pack(pady=8)
for k in range(len(txt_var_variante)) :
    var_variante[k].set(1)
    element2.append((Checkbutton(frame[n], text=txt_var_variante[k], variable=var_variante[k])))
    element2[k].pack(side=LEFT,padx=2)

aff_frame(n)

#2- Nombre de joueur
n+=1
label_nbjoueur = Label(frame[n], text='Nombre de joueur', font=("Arial", 11))
label_nbjoueur.pack()
cb_nbjoueur = Combobox(frame[n], values=data_nbjoueur,state="readonly")
cb_nbjoueur.current(0)
cb_nbjoueur.pack(pady=8)

aff_frame(n)

#3- Mode de jeu
n+=1
label_mdj = Label(frame[n], text='Mode de jeu', font=("Arial", 11))
label_mdj.pack()

aff_frame(n)

n+=1
for k in range(len(data_typemdj)) :
    element = Radiobutton(frame[n], text=data_typemdj[k], variable=resultatmdj, value=k+1)
    element.grid(row=k//2, column=k%2, padx=4,pady=4)

frame[n].pack()

#4- Vitesse
n+=1
label_speed = Label(frame[n], text='Vitesse', font=("Arial", 11))
label_speed.pack()
for k in range(len(data_speed)) :
    var_speed.append(IntVar())
    var_speed[k].set(1)
    element3.append(Checkbutton(frame[n], text=data_speed[k], variable=var_speed[k]))
    element3[k].pack(side=LEFT,pady=8,padx=2)

aff_frame(n)

#5- Date
n+=1
label_date = Label(frame[n], text='Période', font=("Arial", 11))
label_date.pack()
aff_frame(n)

n+=1
label_deb = Label(frame[n], text='Début : ')
label_deb.grid(row=0, column=0, pady=8)
debut = DateEntry(frame[n],date_pattern='dd/mm/y',state="readonly",year=date.today().year, month=date.today().month-1, day=date.today().day)
debut.grid(row=0, column=1, pady=8)
label_fin = Label(frame[n], text='Fin : ')
label_fin.grid(row=1, column=0)
fin = DateEntry(frame[n],date_pattern='dd/mm/y',state="readonly",year=date.today().year, month=date.today().month, day=date.today().day)
fin.grid(row=1, column=1)

frame[n].pack()

#6- Valider
n+=1
validate = Button(frame[n], text='Valider', command=action_button)
validate.pack(pady=10, fill=X)

aff_frame(n)