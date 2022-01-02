import backend
import tkinter as tk  
import tkinter.messagebox
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import ImageTk
import csv
import os
def frontend(res):
    path = os.getcwd()
    
    window = tk.Tk()
     
    #Name the window 
    window.title('Welcome to Quadruple Z')
     
    #Define the dimension of window
    window.geometry('800x800')
    
    #image
    canvas = tk.Canvas(window, height = 200, width = 1000)
    image_file = ImageTk.PhotoImage(file= path + '/Welcome.jpg')
    image = canvas.create_image(0, 0, anchor = 'nw', image = image_file)
    canvas.pack(side='top')
     
    #Title 
    tk.Label(window, text='To Empower People To Make Smart Investment Decisions!!',font=('Arial', 24)).pack()
     
    #Name of entries 
    tk.Label(window, text='Enter the Zip Code for house listings:', font=('Arial', 14)).place(x=10, y=250)
    tk.Label(window, text='Choose the Zip Code from our database', font=('Arial', 14)).place(x=10, y=300)
    tk.Label(window, text='OR', font=('Arial', 14)).place(x=150, y=270)
    tk.Label(window, text='If the search is not successful, please try to type your Zip Code in your console to test (which is highly possible).', fg='red',font=('Arial', 14)).place(x=10, y=400)
    
    
    # Enter zipcode
    live_zipcode = tk.StringVar()
    live_zipcode.set(' ')
    entry_zipcode = tk.Entry(window, textvariable=live_zipcode, font=('Arial', 14))
    entry_zipcode.place(x=280,y=250)
    
    # Dropdown box
    db_zipcode = tk.StringVar(master = window)
    db_zipcode.set('15232')
    
    drop = OptionMenu(window, db_zipcode, '15213',
                      '15232', '15222',
                      '15217', '15219',
                      '19104', '19103',
                      '19122', '19134', '19148')
    drop.pack()
    drop.place(x=280, y=300)
    
    global webscraping_zipcode
    global database_zipcode
    
    def contents():
        global webscraping_zipcode
        global database_zipcode
        webscraping_zipcode = live_zipcode.get()
        database_zipcode = db_zipcode.get()
        
        if webscraping_zipcode == ' ':
            is_livescraping = False
            zip_code = database_zipcode
            
        if webscraping_zipcode != ' ':
            is_livescraping = True
            zip_code = webscraping_zipcode
            
        return zip_code, is_livescraping
            
    def search_zipcode():    
        global webscraping_zipcode
        global database_zipcode
        webscraping_zipcode = live_zipcode.get()
        database_zipcode = db_zipcode.get()
    
    
      
            
        
        root = tk.Tk()
        root.title('Search Completed')
        root.geometry('800x800')
    
        def house_df():
           
            filepath = path + '/result_house.csv'
    
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
            var = StringVar(value = list_of_entries,master= window)
    
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
            return list_of_entries
        
            #houses_testing.houses_info()
            
        
        def race_Img():
            r = Toplevel()
            r.title('Ethnicity Results')
        
            canvas = Canvas(r, width = 1600, height = 800)
            canvas.pack()
            #change to real csv race jpg
            image_file = ImageTk.PhotoImage(file = path + '/race_result.jpg')  
       
            image = canvas.create_image(0, 0, anchor = 'nw',image = image_file)
            r.mainloop()
    
        def school_df():
            
            filepath = path + '/result_school.csv'
    
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
            
        
    
        def price_Img():
            p = Toplevel()
            p.title('Housing price changes results')
    
            canvas = Canvas(p,width = 800, height = 800)
            canvas.pack()
             #change to real csv price jpg
            image_file = ImageTk.PhotoImage(file = path + '/time_series.jpg')  
       
            image = canvas.create_image(0, 0, anchor = 'nw',image = image_file)
            p.mainloop()
    
        summary = tk.Label(root, text=res, font=('Arial',12), width=50, height=50)
        summary.place(x = 10, y = 180)
    
            
        btn = Button(root, text = 'Click here to see house results', command = house_df)
        btn.place(x = 10, y = 20)
        btn = Button(root, text = 'Click here to see housing price changes results', command = price_Img)
        btn.place(x = 10, y = 60)
        btn = Button(root, text = 'Click here to see school results', command = school_df)
        btn.place(x = 10, y = 100)
        btn = Button(root, text = 'Click here to see ethnicity results', command = race_Img)
        btn.place(x = 10, y = 140)
        
        root.mainloop()
        
            
    
        #linked to our database 
    
    # Button for search 
    btn_search = tk.Button(window, text='Search', command=search_zipcode)
    btn_search.place(x=280, y=350)
    
    zip_code, is_livescraping = contents()
    #res = backend.recall(zip_code, is_livescraping)
    
    window.mainloop()
