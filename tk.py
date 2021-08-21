from tkinter import *
from tkinter import ttk
from time import sleep, struct_time
from threading import Thread
from datetime import date
from dataclasses import dataclass
import tkinter.font as tkFont

iids=0

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


nomeGet=""
indirizzoGet=""
numeroGet=""
fatturaGet=""
ricevutaGet=""
importoGet=""
giornoGet=str(today.day)
meseGet=str(today.month)
annoGet=str(today.year)
noteGet=""



"""
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
"""

def startIns():

        
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
            file=open("database.ini","a")
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

    def getEntries(Event):
        global nomeGet
        nomeGet=nome.get()
        global indirizzoGet
        indirizzoGet=indirizzo.get()
        global numeroGet
        numeroGet=numero.get()
        global fatturaGet
        fatturaGet=fattura.get()
        global ricevutaGet
        ricevutaGet=ricevuta.get()
        global importoGet
        importoGet=importo.get()
        global giornoGet
        giornoGet=giorno.get()
        global meseGet
        meseGet=mese.get()
        global annoGet
        annoGet=anno.get()
        global noteGet
        noteGet=note.get("1.0",END)
        print(nomeGet,indirizzoGet,numeroGet,fatturaGet,ricevutaGet,giornoGet,meseGet,annoGet,noteGet)

    
    toplevel=Toplevel(root)
    xlen=620
    ylen=320
    toplevel.geometry("620x320+{}+{}".format(int(root.winfo_width()/2-xlen/2),int(root.winfo_height()/2-ylen/2)))
    toplevel.resizable(0,0)
    toplevel.title("Nuova Fattura")
    photo=PhotoImage(file='C:/Users/betta/Desktop/provina/Database/download.png')
    toplevel.iconphoto(False,photo)
    toplevel.bind('<FocusOut>',getEntries)
        
    #Instancing-----------------------------------------------



    nome=Entry(toplevel,width=23)
    nome.insert(END,nomeGet)
    fattura=Entry(toplevel,width=23,text=fatturaGet)
    fattura.insert(END,fatturaGet)
    ricevuta=Entry(toplevel,width=23,text=ricevutaGet)
    ricevuta.insert(END,ricevutaGet)
    importo=Entry(toplevel,width=7,text=importoGet)
    importo.insert(END,importoGet)
    numero=Entry(toplevel,width=23,text=numeroGet)
    numero.insert(END,numeroGet)
    indirizzo=Entry(toplevel,width=23,text=indirizzoGet)
    indirizzo.insert(END,indirizzoGet)
    giorno=ttk.Combobox(toplevel,values=days,width=5)
    mese=ttk.Combobox(toplevel,values=months,width=5)
    anno=ttk.Combobox(toplevel,values=years,width=5)
    ins=Button(toplevel,text="Inserisci",command=insNew,width=5)
    errore=Label(toplevel,text="⚠Compila tutti i campi prima di continuare⚠",fg="white")
    note=Text(toplevel,height=3,width=27,borderwidth=1,relief=SUNKEN)
    note.insert(END,noteGet)
    
    giorno.set(giornoGet)
    mese.set(meseGet)
    anno.set(annoGet)



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


"""
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
"""



def filterSearch():
    
    param=["","","","","",""]
    toCheck=[0,0,0,0,0,0]
    if getFattura.get()!="":
        param[0]=getFattura.get()
        toCheck[0]=1
    if getRicevuta.get()!="":
        param[1]=getRicevuta.get()
        toCheck[1]=1
    if getGiorno.get()!="":
        param[2]=getGiorno.get()
        toCheck[2]=1
    if getMese.get()!="":
        param[3]=getMese.get()
        toCheck[3]=1
    if getAnno.get()!="":
        param[4]=getAnno.get()
        toCheck[4]=1
    if getNome.get()!="":
        param[5]=getNome.get()
        toCheck[5]=1

    fileRead(param,toCheck)
    
def deleteFun():
    megastringonasgravatapazza=""
    paramsRaw=list(tree.item(tree.focus()).values())[2]
    cosacciaschifosa=tree.item(tree.focus())
    for child in tree.get_children():
        if tree.item(child)==cosacciaschifosa:
            tree.delete(child)
    params=[]
    for element in paramsRaw:
        params.append(str(element))
    file=open("database.ini","r")
    for line in file:
        strings=line.rstrip().split("|") 
        
        for i in range(0,len(strings),1):
            strings[i]=strings[i].rstrip()
        
        if not strings==params:
            megastringonasgravatapazza=megastringonasgravatapazza+line
    file.close()
    file2=open("database.ini","w")    
    file2.write(megastringonasgravatapazza)
    file2.close()

    

def fileRead(param,toCheck):
    
    iids=0
    file=open("database.ini","r")
    for line in file:
        if (not line=="") and (not line=="\n"):
            iids=iids+1
            strings=line.rstrip().split("|")
            for i in range(0,1,8):
                strings[i]=strings[i].rstrip()   
            if toCheck[0]==0:
                param[0]=strings[3]
            if toCheck[1]==0:
                param[1]=strings[4]
            if toCheck[2]==0:
                param[2]=strings[6].split("-")[0]      
            if toCheck[3]==0:
                param[3]=strings[6].split("-")[1]  
            if toCheck[4]==0:
                param[4]=strings[6].split("-")[2]  
            if toCheck[5]==0:
                param[5]=strings[0]

            if  param[0]==strings[3] and param[1]==strings[4] and int(param[2])==int(strings[6].split("-")[0]) and int(param[3])==int(strings[6].split("-")[1]) and int(param[4])==int(strings[6].split("-")[2]) and param[5].upper()==strings[0].upper():
                
                tree.insert(parent="",index=END,iid=iids,values=(strings[0],strings[1],strings[2],strings[3],strings[4],strings[5],strings[6],strings[7]))
            
            
    file.close()


def orderView():
    for i in range(2000,today.year+1):
        for j in range(1,13):
            for y in range(1,32):
                fileRead(["","","{}".format(y),"{}".format(j),"{}".format(i),""],[0,0,1,1,1,0])

def threadFilter():
    tree.delete(*tree.get_children())
    Thread(target=filterSearch).start()
    print(root.winfo_height())
    print(root.winfo_width())
def threadOrder():
    tree.delete(*tree.get_children())
    Thread(target=orderView).start()
    print(root.winfo_width())
    print(root.winfo_height())
    
root=Tk()
root.state("zoomed")
root.geometry("{}x{}".format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.resizable(1,1)

def start():
    try:
        for widget in root.winfo_children():
            if isinstance(widget, Toplevel):
                widget.destroy()
        
    except:
        pass
    startIns()



width = (root.winfo_screenwidth()-root.winfo_screenwidth()/25)/24
height = root.winfo_screenheight()
searchFrame=LabelFrame(root,text="Ricerca",font=("Segoe UI",20))
editFrame=LabelFrame(root,text="Modifica",font=("Segoe UI",20))
getNome=Entry(searchFrame,width=30)
getFattura=Entry(searchFrame,width=30)
getRicevuta=Entry(searchFrame,width=30)
getGiorno=ttk.Combobox(searchFrame,width=4,values=days)
getMese=ttk.Combobox(searchFrame,width=4,values=months)
getAnno=ttk.Combobox(searchFrame,width=4,values=years)
get=Button(searchFrame,text="Cerca elemento",command=threadFilter,width=15,height=2,bg="#78a9ff")
order=Button(searchFrame,text="Ordina Database\n per data",command=threadOrder,width=15,height=2,bg="#a6ffd5")
tree=ttk.Treeview(root,height=int((root.winfo_screenheight()/100)*3))
tree.bind("<<Tree")
new=Button(root,text="nuovo",command=start)

delete=Button(root,text="cancela",command=deleteFun)

tree['columns']=("Nome","Numero","Indirizzo","Fattura","Ricevuta","Importo","Data","Note")
tree.column("#0",width=0,stretch=NO)
tree.column('Nome',    width=int(width)*4)
tree.column('Numero',   width=int(width)*2)
tree.column('Indirizzo',    width=int(width)*5)
tree.column('Fattura',   width=int(width)*2)
tree.column('Ricevuta',   width=int(width)*2)
tree.column('Importo',   width=int(width)*1)
tree.column('Data',    width=int(width)*2)
tree.column('Note',    width=int(width)*6)

tree.heading("#0",text="")
tree.heading("Nome",text="Nome")
tree.heading("Numero",text="Numero")
tree.heading("Indirizzo",text="Indirizzo")
tree.heading("Fattura",text="Fattura")
tree.heading("Ricevuta",text="Ricevuta")
tree.heading("Importo",text="Importo")
tree.heading("Data",text="Data")
tree.heading("Note",text="Note")

searchFrame.grid(row=1,column=0,ipadx=root.winfo_screenwidth()/80,ipady=root.winfo_screenheight()/80,padx=root.winfo_screenwidth()/50)

fontStyle = tkFont.Font(family="Segoe UI", size=11)



Label(searchFrame,text="Nome e Cognome",font=fontStyle).grid(row=2,column=0,padx=50,sticky="W")
getNome.grid(row=3,column=0,padx=50)

Label(searchFrame,text="").grid(row=4,column=0,pady=5)

Label(searchFrame,text="Numero di Fattura",font=fontStyle).grid(row=5,column=0,padx=50,sticky="W")
getFattura.grid(row=6,column=0,padx=50)

Label(searchFrame,text="Numero di Ricevuta",font=fontStyle).grid(row=2,column=1,padx=0,columnspan=3,sticky="W")
getRicevuta.grid(row=3,column=1,columnspan=3)

Label(searchFrame,text="").grid(row=4,column=0,pady=5)

Label(searchFrame,text="Data",font=fontStyle).grid(row=5,column=1,padx=10,columnspan=3)
getGiorno.grid(row=6,column=1,padx=0)
getMese.grid(row=6,column=2,padx=0)
getAnno.grid(row=6,column=3,padx=0)
get.grid(row=3,column=6,padx=10)
order.grid(row=5,column=6,padx=10)
tree.grid(row=0,column=0,padx=root.winfo_screenwidth()/50,pady=15,columnspan=200)
delete.grid(row=10,column=10)
new.grid(row=10,column=11)



root.mainloop()


