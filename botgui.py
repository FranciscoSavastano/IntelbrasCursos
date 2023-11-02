from tkinter import * 
import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
import bot
import os
def fim(nome, num):
    showinfo(message=f'Arquivo salvo com sucesso\nem {os.getcwd()} nome: {nome}{num}.xlsx"')
def crianewwindow(root, pags: int):
        def verdinamic(prefix, suffix, pags):
            for i in range(pags):
                globals()[prefix + str(i) + suffix]
            bot.scraping(pags, dinamico0entry.get(), dinamico1entry.get(), dinamico2entry.get(), dinamico3entry.get())
        
        global btcount
        pags = int(pags)
        if pags != 0:
            if btcount == 0:
                prevrow = 0
                prefix = "dinamico"
                suffix = "entry"
                btcount += 1
                newWindow = Toplevel(root)
                newWindow.title("Exporta Planilha")
                newWindow.geometry("700x200")
                newWindow.resizable(False,False)
                for i in range(4):
                    globals()[prefix + str(i) + suffix] = ttk.Entry(newWindow, width= 75)
                for i in range(pags):
                    ttk.Label(newWindow, text=f"Insira a URL da pagina {i + 1} do site da intelbras").grid(column=0, row=prevrow + i)
                    #magia negra para criar variaveis dinamicas com base no numero de paginas
                    
                    match i:
                        case 0: 
                            dinamico0entry.grid(column=1, row=i)
                        case 1:
                            dinamico1entry.grid(column=1, row=i)
                        case 2:
                            dinamico2entry.grid(column=1, row=i)
                        case 3:
                            dinamico3entry.grid(column=1, row=i)
                void = ttk.Label(newWindow, text ="")
                void.place(relx = 1, rely = 1)
                pages = urlentry = ""
                global pb
                pb = ttk.Progressbar(newWindow, length = 200, mode= 'determinate')
                send = ttk.Button(newWindow, text = "Enviar", command=lambda: [pb.start(7), verdinamic(prefix, suffix, pags)]).place(relx = 0.45, rely = 0.5)

                fakepb = ttk.Progressbar(newWindow, length = 200, mode= 'determinate')
                
                fakepb.place(relx=0.355, rely = 0.7)
            else:
                if 'normal' == root.state():
                        btcount = 0
def gui():
    root = Tk()
    root.geometry('200x200')
    root.title("Exporta Planilha")
    root.resizable(False,False)
    frm = tkinter.Frame(root, height= 300)
    frm.grid(column=0, sticky=tkinter.E + tkinter.W)
    root.grid_columnconfigure(0,weight=1)
    v = DoubleVar()
    global btcount
    btcount = 0
    #ttk.Label(frm, text= "Selecione a quantidade de paginas").grid(column=0, row=2, sticky= 'w')
    selected_option = tkinter.StringVar()
    Ir = [('1 Pagina', int(1)), ('2 Paginas', int(2)), ('3 Paginas',int(3)), ('4 Paginas', int(4))]
    relytemp = 0.05
    for Irv, val in Ir:
        Irrad = Radiobutton(frm,text=Irv, variable=v, value=val, font=('verdana', 10))
        Irrad.place(relx=0.01, rely=relytemp)
        relytemp += 0.08
    pagssend = ttk.Button(frm, text = "Proximo" ,command=lambda:  [crianewwindow(root, v.get() )])
    pagssend.place(relx=0.3, rely=0.5)

    root.mainloop()
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   gui()
