from tkinter import *
from tkinter import ttk
import bot

root = Tk()
root.geometry('800x600')
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Ola mundo!").grid(column=0, row=0)
ttk.Button(frm, text="MORRE PRAGA", command=root.destroy).grid(column=1, row=0)
root.mainloop()