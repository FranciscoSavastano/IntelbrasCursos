from tkinter import *
from tkinter import ttk
from threading import Thread

import bot
def start_main(pags, url):
    t = Thread(target=bot.scraping(), args=(pags.get(),url.get()), daemon=True)
    t.start()
def startpb(pb):
    pb.place(relx=0.65, rely = 0.72)
root = Tk()
root.geometry('800x100')
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Insira a URL do site da intelbras").grid(column=0, row=0)
url = ttk.Entry(frm, width= 100)
url.grid(column=1, row=0)
ttk.Label(frm, text= "Insira a quantidade de paginas").grid(column=0, row=2, sticky= 'w')
pags = ttk.Spinbox(frm, width= 5)
pags.grid(column=1, row=2, sticky= 'w')
ttk.Label(frm, text ="").grid(column = 0, row =6)
fakepb = ttk.Progressbar(frm, length = 250, mode= 'determinate')
pb = ttk.Progressbar(frm, length = 250, mode= 'determinate')
fakepb.place(relx=0.65, rely = 0.72)
pages = urlentry = ""
send = ttk.Button(frm, text = "Enviar", command=lambda: [pb.start(300), startpb(pb), start_main(pags, url)] ).place(relx = 0.5, rely = 0.7)

root.mainloop()