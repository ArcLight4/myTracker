from tkinter import *

#create window
window = Tk()

#customize
window.title('Winamax Tracker - By WB-44')
window.geometry ('600x700')
window.resizable(0, 0)
window.iconbitmap("icon.ico")

#text
label_title = Label(window, text='Choix variante')
#show window
window.mainloop()