from tkinter import *
from tkinter import ttk
from time import sleep
from threading import Thread
from datetime import date

days=[]
months=[]
years=[]
Note=""
s="|"
today=date.today()

for i in range(31):
    days.append("{}".format(i+1))

for i in range(12):
    months.append("{}".format(i+1))

for i in range(100):
    years.append("{}".format(i+2000))

def showErrore():
    errore.place(x=18, y=280)
    errore.config(fg="red",text="⚠ Compila tutti i campi prima di continuare! ⚠")
    sleep(4)
    errore.place_forget()


def showIns():
    errore.place(x=18, y=280)
    errore.config(fg="green",text="✓ Nuova nattura inserita ✓")
    sleep(4)
    errore.place_forget()

def insNew():
    if not nome.get()=="" and not fattura.get()=="" and not importo.get()=="" and not mese.get()=="" and not anno.get()=="" and not ricevuta.get()=="" and not indirizzo.get()=="" and not numero.get()=="":
        file=open("Database.txt","a")
        if note.get("1.0",END)=="\n":
            Note="Nessuna nota\n"
        else:
            Note=note.get("1.0",END)
        

        print("xx"+note.get("1.0",END)+"xx")
        file.write(nome.get().rstrip()+s+numero.get().rstrip()+s+indirizzo.get().rstrip()+s+fattura.get().rstrip()+s+ricevuta.get().rstrip()+s+importo.get().rstrip()+s+giorno.get().rstrip()+"-"+mese.get().rstrip()+"-"+anno.get().rstrip()+s+Note)
        file.close()
        Thread(target=showIns).start()
        nome.delete(0,END)
        fattura.delete(0,END)
        importo.delete(0,END)
        giorno.set(today.day)
        mese.set(today.month)
        anno.set(today.year)    
        numero.delete(0,END)    
        indirizzo.delete(0,END)
        ricevuta.delete(0,END)
        note.delete("1.0",END)
    else:
        Thread(target=showErrore).start()      

#Instancing-----------------------------------------------

toplevel=Tk()
toplevel.geometry("620x320")
toplevel.resizable(0,0)
toplevel.title("Nuova Fattura")
#photo=PhotoImage(file='C:/Users/betta/Desktop/provina/download.png')
#toplevel.iconphoto(False,photo)

nome=Entry(toplevel,width=23)
fattura=Entry(toplevel,width=23)
ricevuta=Entry(toplevel,width=23)
importo=Entry(toplevel,width=7)
numero=Entry(toplevel,width=23)
indirizzo=Entry(toplevel,width=23)
giorno=ttk.Combobox(toplevel,values=days,width=5)
mese=ttk.Combobox(toplevel,values=months,width=5)
anno=ttk.Combobox(toplevel,values=years,width=5)
ins=Button(toplevel,text="Inserisci",command=insNew,width=5)
errore=Label(toplevel,text="⚠Compila tutti i campi prima di continuare⚠",fg="white")
note=Text(toplevel,height=3,width=27,borderwidth=1,relief=SUNKEN)
giorno.set(today.day)
mese.set(today.month)
anno.set(today.year)



#Graphics------------------------------------------------

Label(toplevel, text='Nome Cognome').place(x=18, y=10)
nome.place(x=18, y=32)
Label(toplevel, text='Numero telefonico').place(x=18, y=60)
numero.place(x=18,y=82)
Label(toplevel, text='Indirizzo').place(x=18, y=110)
indirizzo.place(x=18,y=132)
Label(toplevel, text='Note (opzionale)').place(x=18, y=160)
note.place(x=18,y=182)
Label(toplevel, text='Numero fattura').place(x=308, y=10)
fattura.place(x=308,y=32)
Label(toplevel, text='Numero ricevuta').place(x=308, y=60)
ricevuta.place(x=308,y=82)
Label(toplevel, text='Importo').place(x=308, y=110)
importo.place(x=325,y=132)
Label(toplevel,text="€").place(x=308,y=135)
Label(toplevel, text='Giorno').place(x=308, y=160)
giorno.place(x=308, y=182)
Label(toplevel, text='Mese').place(x=373, y=160)
mese.place(x=373, y=182)
Label(toplevel, text='Anno').place(x=438, y=160)
anno.place(x=438, y=182)
ins.place(x=540,y=280)



toplevel.mainloop()



