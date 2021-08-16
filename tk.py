from tkinter import *
from tkinter import ttk
from time import sleep, struct_time
from threading import Thread
from datetime import date
from dataclasses import dataclass

iids=0


today=date.today()

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

def fileRead(param,toCheck):
    iids=0
    file=open("DataBase.txt","r")
    for line in file:
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
            print(strings)  
            tree.insert(parent="",index=END,iid=iids,values=(strings[0],strings[1],strings[2],strings[3],strings[4],strings[5],strings[6],strings[7]))
            
            
    file.close()


def orderView():
    for i in range(2000,today.year+1):
        for j in range(1,13):
            for y in range(1,32):
                fileRead(["","","{}".format(y),"{}".format(j),"{}".format(i),""],[0,0,1,1,1,0])

def threadFilter():
    Thread(target=filterSearch).start()
def threadOrder():
    Thread(target=orderView).start()
    
root=Tk()
root.state("zoomed")
root.geometry("{}x{}".format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.resizable(1,1)
width = (root.winfo_screenwidth()-root.winfo_screenwidth()/100)/24
height = root.winfo_screenheight()
getFattura=Entry(root,width=23)
getRicevuta=Entry(root,width=23)
getGiorno=ttk.Combobox(root,width=4)
getMese=ttk.Combobox(root,width=4)
getAnno=ttk.Combobox(root,width=4)
get=Button(root,text="Cerca",command=threadFilter)
order=Button(root,text="Ordina",command=threadOrder)
tree=ttk.Treeview(root,height=20)
getNome=Entry(root,width=23)
tree['columns']=("Nome","Numero","Indirizzo","Fattura","Ricevuta","Importo","Data","Note")
tree.column("#0",width=0,stretch=NO,)
tree.column('Nome',    width=int(width)*4)
tree.column('Numero',   width=int(width)*2)
tree.column('Indirizzo',    width=int(width)*5)
tree.column('Fattura',   width=int(width)*2)
tree.column('Ricevuta',   width=int(width)*2)
tree.column('Importo',   width=int(width)*1)
tree.column('Data',    width=int(width)*2)
tree.column('Note',    width=int(width)*6)

tree.heading("#0",text="Boh")
tree.heading("Nome",text="Nome")
tree.heading("Numero",text="Numero")
tree.heading("Indirizzo",text="Indirizzo")
tree.heading("Fattura",text="Fattura")
tree.heading("Ricevuta",text="Ricevuta")
tree.heading("Importo",text="Importo")
tree.heading("Data",text="Data")
tree.heading("Note",text="Note")



Label(root,text="Nome e Cognome").grid(row=1,column=0,padx=10)
getNome.grid(row=2,column=0)
Label(root,text="Fattura").grid(row=3,column=0,padx=10)

getFattura.grid(row=4,column=0)
Label(root,text="Ricevuta").grid(row=1,column=1,padx=10,columnspan=3)

getRicevuta.grid(row=2,column=1,columnspan=3)
Label(root,text="Data").grid(row=3,column=1,padx=10,columnspan=3)

getGiorno.grid(row=4,column=1,padx=0)
getMese.grid(row=4,column=2,padx=0)
getAnno.grid(row=4,column=3,padx=0)
get.grid(row=1,column=6)
order.grid(row=1,column=7)
tree.grid(row=0,column=0,padx=root.winfo_screenwidth()/200,pady=15,columnspan=100)


root.mainloop()