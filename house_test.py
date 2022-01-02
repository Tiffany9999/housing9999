import csv
import tkinter as tk
from tkinter import *

filepath = '/Users/marcus/Desktop/95888 Python/Project Code Final/houses.csv'

File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)
del(Data[0])

list_of_entries = []
for x in list(range(0,len(Data))):
        list_of_entries.append(Data[x][5])

root=tk.Tk()
root.title('Houses Information')
root.geometry('500x450')
var = StringVar(value = list_of_entries)
listbox1 = Listbox(root, listvariable = var)
listbox1.grid(row=0, column=0)

def update():
        index = listbox1.curselection()[0]
        zipcodelabel2.config(text = Data[index][0])
        pricelabel2.config(text = Data[index][1])
        bedroomlabel2.config(text = Data[index][2])
        bathroomlabel2.config(text = Data[index][3])
        arealabel2.config(text = Data[index][4])
        addresslabel2.config(text = Data[index][5])
        citylabel2.config(text = Data[index][6])
        statelabel2.config(text = Data[index][7])

        return None 
                        

button1 = Button(root, text='Show house Info', command=update)
button1.grid(row=11,column=0)
zipcodelabel = Label(root,text='Zip Code').grid(row=1,column=0,sticky='w')
pricelabel = Label(root,text='House Price').grid(row=2,column=0,sticky='w')
bedroomlabel = Label(root,text='# Bedrooms').grid(row=3,column=0,sticky='w')
bathroomlabel = Label(root,text='# Bathrooms').grid(row=4,column=0,sticky='w')
arealabel = Label(root,text='Area in sqft').grid(row=5,column=0,sticky='w')
addresslabel = Label(root,text='Address').grid(row=6,column=0,sticky='w')
citylabel = Label(root,text='City').grid(row=7,column=0,sticky='w')
statelabel = Label(root,text='State').grid(row=8,column=0,sticky='w')


zipcodelabel2 = Label(root,text='')
zipcodelabel2.grid(row=1,column=1,sticky='w')

pricelabel2 = Label(root,text='')
pricelabel2.grid(row=2,column=1,sticky='w')

bedroomlabel2 = Label(root,text='')
bedroomlabel2.grid(row=3,column=1,sticky='w')

bathroomlabel2 = Label(root,text='')
bathroomlabel2.grid(row=4,column=1,sticky='w')

arealabel2 = Label(root,text='')
arealabel2.grid(row=5,column=1,sticky='w')

addresslabel2 = Label(root,text='')
addresslabel2.grid(row=6,column=1,sticky='w')

citylabel2 = Label(root,text='')
citylabel2.grid(row=7,column=1,sticky='w')

statelabel2 = Label(root,text='')
statelabel2.grid(row=8,column=1,sticky='w')

        
root.mainloop()
