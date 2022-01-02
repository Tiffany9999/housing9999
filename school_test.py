import csv
import tkinter as tk
from tkinter import *



filepath = '/Users/marcus/Desktop/95888 Python/Project Code Final/schools.csv'

File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)
del(Data[0])

list_of_entries = []
for x in list(range(0,len(Data))):
    list_of_entries.append(Data[x][1])

root=tk.Tk()
root.title('School Information')
root.geometry('500x450')
var = StringVar(value = list_of_entries)
listbox1 = Listbox(root, listvariable = var)
listbox1.grid(row=0, column=0)

def update():
    index = listbox1.curselection()[0]
    zipcodelabel2.config(text = Data[index][0])
    schoollabel2.config(text = Data[index][1])
    MathProficiencylabel2.config(text = Data[index][2])
    ReadingProficicencylabel2.config(text = Data[index][3])
    gradeslabel2.config(text = Data[index][4])
    locationlabel2.config(text = Data[index][5])
    distancelabel2.config(text = Data[index][6])
    studentslabel2.config(text = Data[index][7])
    telephonelabel2.config(text = Data[index][8])
    detailslabel2.config(text = Data[index][9])

    return None 
            

button1 = Button(root, text='Show School Info', command=update)
button1.grid(row=11,column=0)

zipcodelabel = Label(root,text='Zip Code').grid(row=1,column=0,sticky='w')
schoollabel = Label(root,text='school').grid(row=2,column=0,sticky='w')
MathProficiencylabel = Label(root,text='Math Proficiency').grid(row=3,column=0,sticky='w')
ReadingProficicencylabel = Label(root,text='Reading Proficiency').grid(row=4,column=0,sticky='w')
gradeslabel = Label(root,text='Grades').grid(row=5,column=0,sticky='w')
locationlabel = Label(root,text='Location').grid(row=6,column=0,sticky='w')
distancelabel = Label(root,text='Distance').grid(row=7,column=0,sticky='w')
studentslabel = Label(root,text='Students').grid(row=8,column=0,sticky='w')
telephonelabel = Label(root,text='Telephone').grid(row=9,column=0,sticky='w')
detailslabel = Label(root,text='Details').grid(row=10,column=0,sticky='w')

zipcodelabel2 = Label(root,text='')
zipcodelabel2.grid(row=1,column=1,sticky='w')
schoollabel2 = Label(root,text='')
schoollabel2.grid(row=2,column=1,sticky='w')

MathProficiencylabel2 = Label(root,text='')
MathProficiencylabel2.grid(row=3,column=1,sticky='w')

ReadingProficicencylabel2 = Label(root,text='')
ReadingProficicencylabel2.grid(row=4,column=1,sticky='w')

gradeslabel2 = Label(root,text='')
gradeslabel2.grid(row=5,column=1,sticky='w')

locationlabel2 = Label(root,text='')
locationlabel2.grid(row=6,column=1,sticky='w')

distancelabel2 = Label(root,text='')
distancelabel2.grid(row=7,column=1,sticky='w')

studentslabel2 = Label(root,text='')
studentslabel2.grid(row=8,column=1,sticky='w')

telephonelabel2 = Label(root,text='')
telephonelabel2.grid(row=9,column=1,sticky='w')

detailslabel2 = Label(root,text='')
detailslabel2.grid(row=10,column=1,sticky='w')

root.mainloop()
