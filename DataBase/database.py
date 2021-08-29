from tkinter import *
from tkinter import ttk
from time import sleep, struct_time
from threading import Thread
from datetime import date,datetime
import tkinter.font as tkFont
from PIL import Image,ImageTk
import xlsxwriter

iids=0

days=[]
months=[]
years=[]
Note=""
s="|"
today=date.today()

for i in range(31):
    if str(i+1).__len__()==1:
        days.append("0{}".format(i+1))
    else:
        days.append("{}".format(i+1))
for i in range(12):
    if str(i+1).__len__()==1:
        months.append("0{}".format(i+1))
    else:
        months.append("{}".format(i+1))

for i in range(100):
    years.append("{}".format(i+2000))


nomeGet=""
indirizzoGet=""
numeroGet=""
fatturaGet=""
ricevutaGet=""
importoGet=""
giornoGet=""
meseGet=""
annoGet=""
noteGet=""

focused=1

"""
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
"""

def startIns():

    

    def setToday():
        if str(today.day).__len__()==1:
            giorno.set("0{}".format(today.day))
        else:
            giorno.set("{}".format(today.day))
        if str(today.month).__len__()==1:
            mese.set("0{}".format(today.month))
        else:
            mese.set("{}".format(today.month))
        if str(today.year).__len__()==1:
            anno.set("0{}".format(today.year))
        else:
            anno.set("{}".format(today.year))
    def clear():
            nome.delete(0,END)
            fattura.delete(0,END)
            importo.delete(0,END)
            giorno.set("")
            mese.set("")
            anno.set("")    
            numero.delete(0,END)    
            indirizzo.delete(0,END)
            ricevuta.delete(0,END)
            note.delete("1.0",END)
        
    def showErrore():
        errore.place(x=18, y=280)
        errore.config(fg="red",text="⚠ Compila tutti i campi prima di continuare! ⚠")
        sleep(1)
        errore.place_forget()


    def showIns():
        errore.place(x=18, y=280)
        errore.config(fg="green",text="✓ Nuova fattura inserita ✓")
        sleep(1)
        errore.place_forget()

    def insNew():
        if not nome.get()=="" and not importo.get()=="" and not giorno.get()=="" and not mese.get()=="" and not anno.get()=="" and not ricevuta.get()=="" and not indirizzo.get()=="" and not numero.get()=="":
            file=open("database.ini","a")
            if note.get("1.0",END).strip()=="":
                Note="Nessuna nota\n"
            else:
                Note=note.get("1.0",END)
                Note=Note.strip()
                Note=Note+"\n"

            if fattura.get().strip()=="":
                Fattura="/"
            else:
                Fattura=fattura.get()
                Fattura=Fattura.strip()

            file.write(nome.get().rstrip()+s+numero.get().rstrip()+s+indirizzo.get().rstrip()+s+Fattura.rstrip()+s+ricevuta.get().rstrip()+s+importo.get().rstrip()+s+giorno.get().rstrip()+"-"+mese.get().rstrip()+"-"+anno.get().rstrip()+s+Note)
            file.close()
            Thread(target=showIns).start()
            nome.delete(0,END)
            fattura.delete(0,END)
            importo.delete(0,END)
            giorno.set("")
            mese.set("")
            anno.set("")    
            numero.delete(0,END)    
            indirizzo.delete(0,END)
            ricevuta.delete(0,END)
            note.delete("1.0",END)
            elements()  
        elif not nome.get()=="" and not fattura.get()=="" and not importo.get()=="" and not mese.get()=="" and not anno.get()=="" and not indirizzo.get()=="" and not numero.get()=="":
            file=open("database.ini","a")
            if note.get("1.0",END).strip()=="":
                Note="Nessuna nota\n"
            else:
                Note=note.get("1.0",END)
                Note=Note.strip()
                Note=Note+"\n"


            if ricevuta.get().strip()=="":
                Ricevuta="/"
            else:
                Ricevuta=ricevuta.get()
                Ricevuta=Ricevuta.strip()

            file.write(nome.get().rstrip()+s+numero.get().rstrip()+s+indirizzo.get().rstrip()+s+fattura.get().rstrip()+s+Ricevuta.rstrip()+s+importo.get().rstrip()+s+giorno.get().rstrip()+"-"+mese.get().rstrip()+"-"+anno.get().rstrip()+s+Note)
            file.close()
            Thread(target=showIns).start()
            nome.delete(0,END)
            fattura.delete(0,END)
            importo.delete(0,END)
            giorno.set("")
            mese.set("")
            anno.set("")    
            numero.delete(0,END)    
            indirizzo.delete(0,END)
            ricevuta.delete(0,END)
            note.delete("1.0",END)
            elements()         
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

    def onClosing():
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
        toplevel.destroy()

    
    toplevel=Toplevel(root)
    xlen=620
    ylen=320
    toplevel.geometry("620x320+{}+{}".format(int(root.winfo_width()/2-xlen/2),int(root.winfo_height()/2-ylen/2)))
    toplevel.resizable(0,0)
    toplevel.title("Nuova Fattura")
    try:
        photo=PhotoImage(file='download.png')
        toplevel.iconphoto(False,photo)
    except:
        pass
    toplevel.bind('<FocusOut>',getEntries)
    toplevel.protocol("WM_DELETE_WINDOW", onClosing)
        
    #Instancing-----------------------------------------------



    nome=Entry(toplevel,width=27)
    nome.insert(END,nomeGet)
    fattura=Entry(toplevel,width=27,text=fatturaGet)
    fattura.insert(END,fatturaGet)
    ricevuta=Entry(toplevel,width=27,text=ricevutaGet)
    ricevuta.insert(END,ricevutaGet)
    importo=Entry(toplevel,width=7,text=importoGet)
    importo.insert(END,importoGet)
    numero=Entry(toplevel,width=27,text=numeroGet)
    numero.insert(END,numeroGet)
    indirizzo=Entry(toplevel,width=27,text=indirizzoGet)
    indirizzo.insert(END,indirizzoGet)
    giorno=ttk.Combobox(toplevel,values=days,width=5)
    mese=ttk.Combobox(toplevel,values=months,width=5)
    anno=ttk.Combobox(toplevel,values=years,width=5)
    ins=Button(toplevel,text="Aggiungi",command=insNew,width=10,height=1,bg="#85ff9d")
    todayButt=Button(toplevel,text="Oggi",command=setToday,width=10,bg="#78a9ff")
    clearButt=Button(toplevel,text="Pulisci",command=clear,width=10,height=1,bg="#fff382")
    errore=Label(toplevel,text="⚠Compila tutti i campi prima di continuare⚠",fg="white")
    note=Text(toplevel,height=3,width=27,borderwidth=1,font=fontStyle)
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
    todayButt.place(x=520, y=182)
    ins.place(x=520,y=282)
    clearButt.place(x=420,y=282)

    toplevel.mainloop()


"""
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
"""




def elements():
        els["text"]="Calcolando..."
        file=open("database.ini","r")
        num=0
        for line in file: 
            num=num+1
        els["text"]=str(num)+" elementi"




def filterSearch():
    flag.config(text="!!!Aspetta!!!")
    for child in searchFrame.winfo_children():
                if child.winfo_class()=="Button":
                    child["state"]=DISABLED
    param=["","","","","",""]
    toCheck=[0,0,0,0,0,0]
    if getFattura.get().strip()!="":
        param[0]=getFattura.get().strip()
        toCheck[0]=1
    if getRicevuta.get().strip()!="":
        param[1]=getRicevuta.get().strip()
        toCheck[1]=1
    if getGiorno.get().strip()!="":
        param[2]=getGiorno.get().strip()
        toCheck[2]=1
    if getMese.get().strip()!="":
        param[3]=getMese.get().strip()
        toCheck[3]=1
    if getAnno.get().strip()!="":
        param[4]=getAnno.get().strip()
        toCheck[4]=1
    if getNome.get().strip()!="":
        param[5]=getNome.get().strip()
        toCheck[5]=1

    fileRead(param,toCheck)
    for child in searchFrame.winfo_children():
                if child.winfo_class()=="Button":
                    child["state"]=NORMAL
    flag.config(text="")
    
def deleteFun():
    
    flag.config(text="!!!Aspetta!!!")
    onoff=None
    megastringonasgravatapazza=""
    paramsRaw=list(tree.item(tree.focus()).values())[2]
    cosacciaschifosa=tree.item(tree.focus())


    for row in tree.get_children():
        if tree.item(row)==cosacciaschifosa:
            tree.delete(row)


    if showNome["state"]==DISABLED:
        onoff=False
    for child in editFrame.winfo_children():
        if child.winfo_class()=="Entry":
            child["state"]=NORMAL
            child.delete(0,END)
        elif child.winfo_class()=="Text":
            child["state"]=NORMAL
            child.delete("1.0",END)
    if onoff==False:
        for child in editFrame.winfo_children():
            if (child.winfo_class()=="Entry" or child.winfo_class()=="Text"):
                    child["state"]=DISABLED
                    if child.winfo_class()=="Text":
                        child["background"]="#F0F0F0"
                        child["foreground"]="#6D6D6D"
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
    flag.config(text="")
    elements()

def editFun():
    flag.config(text="!!!Aspetta!!!")
    megastringonasgravatapazza=""
    if root.winfo_screenheight()>800:
        if showNote.get("1.0",END).strip()=="":
                Note="Nessuna nota\n"
        else:
                Note=showNote.get("1.0",END)
                Note=Note.strip()
                Note=Note+"\n"

        if showRicevuta.get().strip()=="":
            Ricevuta="/"
        else:
            Ricevuta=showRicevuta.get()
            Ricevuta=Ricevuta.strip()


        if showFattura.get().strip()=="":
            Fattura="/"
        else:
            Fattura=showFattura.get()
            Fattura=Fattura.strip()
        
        editString=showNome.get().rstrip()+s+showNumero.get().rstrip()+s+showIndirizzo.get().rstrip()+s+Fattura+s+Ricevuta+s+showImporto.get().rstrip()+s+showGiorno.get().rstrip()+"-"+showMese.get().rstrip()+"-"+showAnno.get().rstrip()+s+Note
    else:
        if showNote.get().strip()=="":
                Note="Nessuna nota\n"
        else:
                Note=showNote.get()
        editString=showNome.get().rstrip()+s+showNumero.get().rstrip()+s+showIndirizzo.get().rstrip()+s+showFattura.get().rstrip()+s+showRicevuta.get().rstrip()+s+showImporto.get().rstrip()+s+showGiorno.get().rstrip()+"-"+showMese.get().rstrip()+"-"+showAnno.get().rstrip()+s+Note.rstrip()+"\n"
    paramsRaw=list(tree.item(tree.focus()).values())[2]
    cosacciaschifosa=tree.item(tree.focus())
    

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
        else:
            megastringonasgravatapazza=megastringonasgravatapazza+editString
           
    file.close()
    for row in tree.get_children():
                if tree.item(row)==cosacciaschifosa:
                    tree.item(row,values=(editString.rstrip().split("|")))
    file2=open("database.ini","w")    
    file2.write(megastringonasgravatapazza)
    file2.close()
    flag.config(text="")
    



def showIns(event):
    onoff=None
    if showNome["state"]==DISABLED:
        onoff=False
    for child in editFrame.winfo_children():
        if child.winfo_class()=="Entry":
            child["state"]=NORMAL
            child.delete(0,END)

        elif child.winfo_class()=="Text":
            child["state"]=NORMAL
            child.delete("1.0",END)

    paramsRaw=list(tree.item(tree.focus()).values())[2]
    params=[]
    for element in paramsRaw:
        params.append(str(element))

    if params!=[]:
        showNome.insert(END,params[0])
        showNumero.insert(END,params[1])
        showIndirizzo.insert(END,params[2])
        if params[3].strip()=="/":
            showFattura.insert(END,"")
        else:
            showFattura.insert(END,params[3])

        if params[4].strip()=="/":
            showRicevuta.insert(END,"")
        else:
            showRicevuta.insert(END,params[4])

        
        showImporto.insert(END,params[5])
        showGiorno.insert(END,params[6].split("-")[0])
        showMese.insert(END,params[6].split("-")[1])  
        showAnno.insert(END,params[6].split("-")[2])  
        if params[7].strip()=="Nessuna nota":
            showNote.insert(END,"")
        else:
            showNote.insert(END,params[7])

    if onoff==False:
        for child in editFrame.winfo_children():
            if (child.winfo_class()=="Entry" or child.winfo_class()=="Text"):
                    child["state"]=DISABLED
                    if child.winfo_class()=="Text":
                        child["background"]="#F0F0F0"
                        child["foreground"]="#6D6D6D"



def onoffFun(event):
    if showNome["state"]==NORMAL:
        active["image"]=openLock
        for child in editFrame.winfo_children():
            if child.winfo_class()=="Entry" or child.winfo_class()=="Text" or child.winfo_class()=="Button":
                child["state"]=DISABLED
                if child.winfo_class()=="Text":
                    child["background"]="#F0F0F0"
                    child["foreground"]="#6D6D6D"
    else:
        active["image"]=closedLock
        for child in editFrame.winfo_children():
            if child.winfo_class()=="Entry" or child.winfo_class()=="Text" or child.winfo_class()=="Button":
                child["state"]=NORMAL
                if child.winfo_class()=="Text":
                    child["background"]="White"
                    child["foreground"]="Black"


def fileRead(param,toCheck):
    iids=0
    file=open("database.ini","r")
    for line in file:
        if (not line=="") and (not line=="\n"):
            
            strings=line.rstrip().split("|")
            for i in range(0,1,8):
                strings[i]=strings[i].strip()   
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
            if  strings[3].upper().find(param[0].upper())!=-1 and strings[4].upper().find(param[1].upper())!=-1 and str(param[2])==str(strings[6].split("-")[0]) and str(param[3])==str(strings[6].split("-")[1]) and str(param[4])==str(strings[6].split("-")[2]) and strings[0].upper().find(param[5].upper())!=-1:
                iids=iids+1
                tree.insert(parent="",index=END,values=(strings[0],strings[1],strings[2],strings[3],strings[4],strings[5],strings[6],strings[7]))
            
            
    file.close()


def orderView():
    flag.config(text="!!!Aspetta!!!")
    for child in searchFrame.winfo_children():
                if child.winfo_class()=="Button":
                    child["state"]=DISABLED

    toSort=[]
    file=open("database.ini","r")
    for line in file:
        if (not line=="") and (not line=="\n"):
            toSort.append(line.rstrip().split("|"))
    
    toSortDate=[]
    for i in range(0,toSort.__len__(),1):
        swapper=toSort[i][6].split("-")
        swaptemp=swapper[0]
        swapper[0]=swapper[2]
        swapper[2]=swaptemp
        if swapper[1].__len__()==1:
            swapper[1]="0"+swapper[1]
        if swapper[2].__len__()==1:
            swapper[2]="0"+swapper[2]
        toSortDate.append(str(swapper[0])+str(swapper[1])+str(swapper[2]))




    for i in range(0,toSort.__len__()-1,1):
        for j in range(0,toSort.__len__()-1,1):
            if(int(toSortDate[j])>int(toSortDate[j+1])):
                temp=toSort[j]
                toSort[j]=toSort[j+1]
                toSort[j+1]=temp

                tempDate=toSortDate[j]
                toSortDate[j]=toSortDate[j+1]
                toSortDate[j+1]=tempDate
    for i in range(0,toSort.__len__(),1):
        tree.insert(parent="",index=END,values=(toSort[i]))
    file.close()
    for child in searchFrame.winfo_children():
                if child.winfo_class()=="Button":
                    child["state"]=NORMAL
    flag.config(text="")

def threadFilter():
   
    onoff=None
    if showNome["state"]==DISABLED:
        onoff=False
    for child in editFrame.winfo_children():
                if child.winfo_class()=="Entry":
                    child["state"]=NORMAL
                    child.delete(0,END)
                elif child.winfo_class()=="Text":
                    child["state"]=NORMAL
                    child.delete("1.0",END)
    if onoff==False:
        for child in editFrame.winfo_children():
            if (child.winfo_class()=="Entry" or child.winfo_class()=="Text"):
                    child["state"]=DISABLED
                    if child.winfo_class()=="Text":
                        child["background"]="#F0F0F0"
                        child["foreground"]="#6D6D6D"
    
    tree.delete(*tree.get_children())
    filterSearch()


def threadOrder():
    
    onoff=None
    if showNome["state"]==DISABLED:
        onoff=False
    for child in editFrame.winfo_children():
                if child.winfo_class()=="Entry":
                    child["state"]=NORMAL
                    child.delete(0,END)
                elif child.winfo_class()=="Text":
                    child["state"]=NORMAL
                    child.delete("1.0",END)
    if onoff==False:
        for child in editFrame.winfo_children():
            if (child.winfo_class()=="Entry" or child.winfo_class()=="Text"):
                    child["state"]=DISABLED
                    if child.winfo_class()=="Text":
                        child["background"]="#F0F0F0"
                        child["foreground"]="#6D6D6D"
    tree.delete(*tree.get_children())
    orderView()
    
def threadEdit():
    editFun()
    flag.config(text="")

def start():
    try:
        for widget in root.winfo_children():
            if isinstance(widget, Toplevel):
                widget.destroy()
    except:
        pass
    startIns()

def threadWait():
    flag.config(text="!!!Aspetta!!!")

root=Tk()
root.state("zoomed")
root.geometry("{}x{}".format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.title("DataBase")
try:
    root.iconbitmap("iconona.ico")
except:
    pass

root.resizable(1,1)
fontStyle = tkFont.Font(family="Segoe UI", size=9)
width = (root.winfo_screenwidth()-root.winfo_screenwidth()/25)/24
height = root.winfo_screenheight()
searchFrame=LabelFrame(root,text="Ricerca",font=("Segoe UI",16))
editFrame=LabelFrame(root,text="Modifica",font=("Segoe UI",16))



getNome=Entry(searchFrame,font=fontStyle,width=int(root.winfo_screenwidth()/75))
getFattura=Entry(searchFrame,font=fontStyle,width=int(root.winfo_screenwidth()/75))
getRicevuta=Entry(searchFrame,font=fontStyle,width=int(root.winfo_screenwidth()/75))
if int(root.winfo_screenwidth()/480)<4:
    getGiorno=ttk.Combobox(searchFrame,font=fontStyle,width=4,values=days)
    getMese=ttk.Combobox(searchFrame,font=fontStyle,width=4,values=months)
    getAnno=ttk.Combobox(searchFrame,font=fontStyle,width=4,values=years)
else:
    getGiorno=ttk.Combobox(searchFrame,font=fontStyle,width=int(root.winfo_screenwidth()/480),values=days)
    getMese=ttk.Combobox(searchFrame,font=fontStyle,width=int(root.winfo_screenwidth()/480),values=months)
    getAnno=ttk.Combobox(searchFrame,font=fontStyle,width=int(root.winfo_screenwidth()/480),values=years)




if root.winfo_screenheight()>800:
    new=Button(root,text="Aggiungi\nelemento",command=start,width=int(root.winfo_screenwidth()/120),height=2,bg="#85ff9d")
    get=Button(searchFrame,text="Cerca\nelemento",command=threadFilter,width=int(root.winfo_screenwidth()/120),height=2,bg="#78a9ff")
    order=Button(searchFrame,text="Ordina Database\n per data",command=threadOrder,width=int(root.winfo_screenwidth()/120),height=2,bg="#bdfbff")
    delete=Button(editFrame,text="Elimina\nelemento",command=deleteFun,width=int(root.winfo_screenwidth()/120),height=2,bg="#ff6b6b")
    edit=Button(editFrame,text="Modifica\nelemento",command=threadEdit,width=int(root.winfo_screenwidth()/120),height=2,bg="#fff382")
else:

    new=Button(root,text="Aggiungi",command=start,width=int(root.winfo_screenwidth()/120),height=2,bg="#85ff9d")
    get=Button(searchFrame,text="Cerca",command=threadFilter,width=int(root.winfo_screenwidth()/200),height=1,bg="#78a9ff")
    order=Button(searchFrame,text="Ordina",command=threadOrder,width=int(root.winfo_screenwidth()/200),height=1,bg="#bdfbff")
    delete=Button(editFrame,text="Elimina",command=deleteFun,width=int(root.winfo_screenwidth()/200),height=1,bg="#ff6b6b")
    edit=Button(editFrame,text="Modifica",command=threadEdit,width=int(root.winfo_screenwidth()/200),height=1,bg="#fff382")


treeFrame=Frame(root)
treeScroll=Scrollbar(treeFrame)
tree=ttk.Treeview(treeFrame,height=int((root.winfo_screenheight()/100)*3),yscrollcommand=treeScroll.set)
tree.bind("<<TreeviewSelect>>",showIns)
flag=Label(text="",fg="red",font=("Segoe UI",12,"bold"))
treeScroll.config(command=tree.yview)

showNome=Entry(editFrame,font=fontStyle,width=int(root.winfo_screenwidth()/75))
showIndirizzo=Entry(editFrame,font=fontStyle,width=int(root.winfo_screenwidth()/75))
showNumero=Entry(editFrame,font=fontStyle,width=int(root.winfo_screenwidth()/75))
showFattura=Entry(editFrame,font=fontStyle,width=int(root.winfo_screenwidth()/75))
showRicevuta=Entry(editFrame,font=fontStyle,width=int(root.winfo_screenwidth()/75))
showImporto=Entry(editFrame,font=fontStyle,width=int(root.winfo_screenwidth()/75/3))
if int(root.winfo_screenwidth()/480)<4:
    showGiorno=Entry(editFrame,font=fontStyle,width=4)
    showMese=Entry(editFrame,font=fontStyle,width=4)
    showAnno=Entry(editFrame,font=fontStyle,width=4)
else:
    showGiorno=Entry(editFrame,font=fontStyle,width=int(root.winfo_screenwidth()/360))
    showMese=Entry(editFrame,font=fontStyle,width=int(root.winfo_screenwidth()/360))
    showAnno=Entry(editFrame,font=fontStyle,width=int(root.winfo_screenwidth()/360))

if root.winfo_screenheight()>800:
    showNote=Text(editFrame,width=int(root.winfo_screenwidth()/75),font=fontStyle,height=2)
    showNote["background"]="#F0F0F0"
    showNote["foreground"]="#6D6D6D"
else:
    showNote=Entry(editFrame,width=int(root.winfo_screenwidth()/75),font=fontStyle)

els=Label(root)


img = Image.open("lucchettino.png")
img = img.resize((30,30), Image.ANTIALIAS)

img2 = Image.open("lucchettino_chiuso.png")
img2 = img2.resize((30,30), Image.ANTIALIAS)


openLock=ImageTk.PhotoImage(img)
closedLock=ImageTk.PhotoImage(img2)

active=Label(editFrame,image=openLock,font=("segoeUI",14))
active.bind("<Button-1>",onoffFun)

for child in editFrame.winfo_children():
    if child.winfo_class()=="Entry" or child.winfo_class()=="Text" or child.winfo_class()=="Button":
                child["state"]=DISABLED


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




if root.winfo_screenheight()>800:
    searchFrame.grid(row=1,column=0,ipadx=int(root.winfo_screenwidth()/80),ipady=int(root.winfo_screenheight()/50),padx=int(root.winfo_screenwidth()/50),rowspan=3)
    editFrame.grid(row=1,column=1,ipadx=int(root.winfo_screenwidth()/120),ipady=int(root.winfo_screenheight()/80),rowspan=3)
else:
    searchFrame.grid(row=1,column=0,ipadx=int(root.winfo_screenwidth()/80),ipady=int(root.winfo_screenheight()/100),padx=int(root.winfo_screenwidth()/50),rowspan=3)
    editFrame.grid(row=1,column=1,ipadx=int(root.winfo_screenwidth()/120),ipady=int(root.winfo_screenheight()/100),rowspan=3)
#------------------------------------------------------------------------------------

if root.winfo_screenheight()>800:
   Label(searchFrame,text="").grid(row=1,column=0,pady=int(root.winfo_screenheight()/200))
else:
    pass


Label(searchFrame,text="Nome e Cognome",font=fontStyle).grid(row=2,column=0,padx=int(root.winfo_screenwidth()/40),sticky="W")
getNome.grid(row=3,column=0,padx=int(root.winfo_screenwidth()/40))

Label(searchFrame,text="").grid(row=4,column=0,pady=int(root.winfo_screenheight()/100))

Label(searchFrame,text="Numero Fattura",font=fontStyle).grid(row=5,column=0,padx=int(root.winfo_screenwidth()/40),sticky="W")
getFattura.grid(row=6,column=0,padx=int(root.winfo_screenwidth()/40))
#-------------------------------------------------------------------------------------

Label(searchFrame,text="").grid(row=4,column=0,pady=int(root.winfo_screenheight()/100))

Label(searchFrame,text="Numero Ricevuta",font=fontStyle).grid(row=2,column=1,padx=0,columnspan=3,sticky="W")
getRicevuta.grid(row=3,column=1,columnspan=3,sticky="W")

Label(searchFrame,text="").grid(row=4,column=0,pady=int(root.winfo_screenheight()/100))

Label(searchFrame,text="Data",font=fontStyle).grid(row=5,column=1,padx=0,columnspan=3)
getGiorno.grid(row=6,column=1,padx=0)
getMese.grid(row=6,column=2,padx=0)
getAnno.grid(row=6,column=3,padx=0)
#--------------------------------------------------------------------------------------
Label(searchFrame,text="").grid(row=3,column=5,padx=int(root.winfo_screenwidth()/200))
get.grid(row=3,column=6,padx=0)
Label(searchFrame,text="").grid(row=5,column=5,padx=int(root.winfo_screenwidth()/200))
order.grid(row=5,column=6,padx=0)
#--------------------------------------------------------------------------------------
treeFrame.grid(row=0,column=0,padx=int(root.winfo_screenwidth()/50),pady=15,columnspan=200)
tree.pack(side=LEFT)
treeScroll.pack(side=RIGHT,fill=Y)

flag.grid(row=1,column=3,padx=int(root.winfo_screenwidth()/3/2/8))
els.grid(row=2,column=3,padx=int(root.winfo_screenwidth()/3/2/8))
new.grid(row=3,column=3,padx=int(root.winfo_screenwidth()/3/2/8))





if root.winfo_screenheight()>800:
   Label(editFrame,text="").grid(row=1,column=0,pady=int(root.winfo_screenheight()/200))
else:
    pass

Label(editFrame,text="").grid(row=4,column=0,padx=int(root.winfo_screenwidth()/120),pady=int(root.winfo_screenheight()/100))

Label(editFrame,text="Nome e Cognome",font=fontStyle).grid(row=2,column=1,padx=int(root.winfo_screenwidth()/100),sticky="W")
showNome.grid(row=3,column=1,padx=int(root.winfo_screenwidth()/100))



Label(editFrame,text="Numero Telefono",font=fontStyle).grid(row=5,column=1,padx=int(root.winfo_screenwidth()/100),sticky="W")
showNumero.grid(row=6,column=1,padx=int(root.winfo_screenwidth()/100))

#-------------------------------------------------------------------------------------------------



Label(editFrame,text="Indirizzo",font=fontStyle).grid(row=2,column=2,padx=int(root.winfo_screenwidth()/100),sticky="W")
showIndirizzo.grid(row=3,column=2,padx=int(root.winfo_screenwidth()/100))

Label(editFrame,text="N° Fattura",font=fontStyle).grid(row=5,column=2,padx=int(root.winfo_screenwidth()/100),sticky="W")
showFattura.grid(row=6,column=2,padx=int(root.winfo_screenwidth()/100))

#-------------------------------------------------------------------------------------------------

Label(editFrame,text="Importo",font=fontStyle).grid(row=2,column=3,padx=int(root.winfo_screenwidth()/100),sticky="W",columnspan=15)
Label(editFrame,text="€",font=fontStyle).grid(row=3,column=3,sticky="E")
showImporto.grid(row=3,column=4,sticky="W")

Label(editFrame,text="N° Ricevuta",font=fontStyle).grid(row=5,column=3,padx=int(root.winfo_screenwidth()/100),sticky="W",columnspan=15)
showRicevuta.grid(row=6,column=3,padx=int(root.winfo_screenwidth()/100),columnspan=15)

#--------------------------------------------------------------------------------------------


Label(editFrame,text="Data",font=fontStyle).grid(row=2,column=20,padx=int(root.winfo_screenwidth()/100),columnspan=3)
showGiorno.grid(row=3,column=20,padx=int(root.winfo_screenwidth()/100/3),sticky="E")
showMese.grid(row=3,column=21,padx=int(root.winfo_screenwidth()/100/3))
showAnno.grid(row=3,column=22,padx=int(root.winfo_screenwidth()/100/3),sticky="W")


Label(editFrame,text="Note",font=fontStyle).grid(row=5,column=20,padx=int(root.winfo_screenwidth()/100),columnspan=3,sticky="W")
showNote.grid(row=6,column=20,padx=int(root.winfo_screenwidth()/100),columnspan=3)


delete.grid(row=3,column=40)
edit.grid(row=5,column=40)

active.grid(row=3,column=50,rowspan=3,padx=int(root.winfo_screenwidth()/100))




elements()


root.mainloop()


