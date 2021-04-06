from tkinter import *
from tkinter import ttk
import sqlite3

""" Function for myframe1 i.e insert new material. The first frame has a markdown 
widget to select the material name and enter the weight.
 """

def send_to_processing():
    name_entry = str(clicked.get())
    weight_entry = float(weight_text.get())
    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.execute("UPDATE processing SET weight = weight + ? WHERE Name = ?", (weight_entry, name_entry))
    conn.commit()


""" Function for myFrame2. The Processing Frame """

#___________________________________PROCESSING FUNCTION______________________________________________________________

def view_command_processing():
    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.execute("SELECT id, Name, weight, ROUND(weight/wt) AS Number FROM processing WHERE NOT weight = 0.0")
    rows=cur.fetchall()
    list_processing.delete(0, END) 
    for row in rows:
        list_processing.insert(END,row)

def get_selected_row_process(event):
    try:
        global selected_tuple_2
        index = list_processing.curselection()[0]
        selected_tuple_2 = list_processing.get(index)
        entry_processing_name.delete(0,END)
        entry_processing_name.insert(END,selected_tuple_2[1])
        entry_processing_weight.delete(0, END)
        entry_processing_weight.insert(END,selected_tuple_2[2])
        entry_processing_number.delete(0, END)
        entry_processing_number.insert(END,selected_tuple_2[3])
    except IndexError:
        pass

def send_to_plating():
    name_plat = str(name_to_plat.get())
    weight_plat = float(weight_to_plat.get())
    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.execute("UPDATE processing SET weight = weight - ? WHERE Name = ?", (weight_plat, name_plat))
    conn.commit()
    cur.execute("UPDATE plating SET weight = weight + ? WHERE Name = ?", (weight_plat, name_plat))
    conn.commit()


#___________________________________PLATING FUNCTION______________________________________________________________

def view_command_plating():
    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.execute("SELECT id, Name, weight, ROUND(weight/wt) AS Number FROM plating WHERE NOT weight = 0.0")
    rows=cur.fetchall()
    list_plating.delete(0, END) 
    for row in rows:
        list_plating.insert(END,row)   

def get_selected_row_plating(event):
    try:
        global selected_tuple_3
        index = list_plating.curselection()[0]
        selected_tuple_3 = list_plating.get(index)
        entry_plating_name.delete(0,END)
        entry_plating_name.insert(END,selected_tuple_3[1])
        entry_plating_weight.delete(0, END)
        entry_plating_weight.insert(END,selected_tuple_3[2])
        entry_plating_number.delete(0, END)
        entry_plating_number.insert(END,selected_tuple_3[3])
    except IndexError:
        pass

def send_to_toPack():
    name_topack = str(name_to_topack.get())
    weight_topack = float(weight_to_topack.get())
    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.execute("UPDATE plating SET weight = weight - ? WHERE Name = ?", (weight_topack, name_topack))
    conn.commit()
    cur.execute("UPDATE topack SET weight = weight + ? WHERE Name = ?", (weight_topack, name_topack))
    conn.commit()

# __________________________________TOPACK FUNCTION________________________________________________________

def view_command_toPack():
    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.execute("SELECT id, Name, weight, ROUND(weight/wt) AS quantity FROM topack WHERE NOT weight = 0.0")
    rows=cur.fetchall()
    list_toPack.delete(0, END) 
    for row in rows:
        list_toPack.insert(END,row)

def get_selected_row_topack(event):
    try:
        global selected_tuple_4
        index = list_toPack.curselection()[0]
        selected_tuple_4 = list_toPack.get(index)
        entry_toPack_name.delete(0,END)
        entry_toPack_name.insert(END,selected_tuple_4[1])
        entry_toPack_weight.delete(0, END)
        entry_toPack_weight.insert(END,selected_tuple_4[2])
        entry_toPack_number.delete(0, END)
        entry_toPack_number.insert(END,selected_tuple_4[3])
    except IndexError:
        pass

def mat_dictionary():
    mylist=[(1,'Material 1',0.035,0,0), (2,'Material 2',0.021,0,0), (3,'Material 3',0.013,0,0), (4,'Material 4',0.035,0,0), (5,'Material 5',0.065,0,0), (6,'Material 6',0.036,0,0), (7,'Material 7',0.05,0,0), (8,'Material 8',0.024,0,0), (9,'Material 9',0.017,0,0), (10,'Material 10',0.035,0,0), (11,'Material 11',0.006,0,0), (12,'Material 12',0.012,0,0), (13,'Material 13',0.017,0,0), (14,'Material 14',0.005,0,0), (15,'Material 15',0.0044,0,0), (16,'Material 16',0.057,0,0), (17,'Material 17',0.007,0,0), (18,'Material 18',0.24,0,0), (19,'Material 19',0.0237,0,0), (20,'Material 20',0.18,0,0), (21,'Material 21',0.095,0,0), (22,'Material 22',0.09,0,0),(23,'Material 23',0.058,0,0), (24,'Material 24',0.02,0,0), (25,'Material 25',0.087,0,0), (26,'Material 26',0.058,0,0), (27,'Material 27',0.098,0,0), (28,'Material 28',0.042,0,0), (29,'Material 29',0.021,0,0), (30,'Material 30',0.021,0,0), (31,'Material 31',0.122,0,0)]
    list1 = []
    list2 = []
    for i in mylist:
        list1.append(i[1])
        list2.append(i[2])
    d={}
    for key in list1: 
        for value in list2: 
            d[key] = value 
            list2.remove(value) 
            break  
    return d




def send_to_company():
    name_pack= str(name_to_pack.get())
    weight_pack = float(weight_to_pack.get())

    b = mat_dictionary()
    wei = b[name_pack]
    wei1 = round(wei * weight_pack)

    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.execute("UPDATE topack SET weight = weight - ? WHERE Name = ?", (wei1, name_pack))
    conn.commit()



# _________________________________TOTAL________________________________________________________

def total_view():
    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.execute("SELECT Name, SUM(weight), ROUND(SUM(weight/wt)) FROM (SELECT * FROM processing UNION ALL SELECT * FROM plating UNION ALL SELECT * FROM topack) GROUP BY Name ")
    rows=cur.fetchall()
    list_total.delete(0, END)
    for row in rows:
        list_total.insert(END,row)


root = Tk()
root.title('Tabs')
root.geometry("1000x500")

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)
style = ttk.Style()                     
current_theme =style.theme_use()
style.theme_settings(current_theme, {"TNotebook.Tab": {"configure": {"padding": [20, 5]}}})  


myFrame1= Frame(my_notebook, width=1000, height=500)
myFrame2= Frame(my_notebook, width=1000, height=500)
myFrame3= Frame(my_notebook, width=1000, height=500)
myFrame4= Frame(my_notebook, width=1000, height=500)
myFrame5= Frame(my_notebook, width=1000, height=500)



""" myFrame1.pack(fill='both', expand=1)
myFrame2.pack(fill='both', expand=1)
myFrame3.pack(fill='both', expand=1)
myFrame4.pack(fill='both', expand=1)
myFrame5.pack(fill='both', expand=1)
 """

my_notebook.add(myFrame1, text='Entry')
my_notebook.add(myFrame2, text='Processing')
my_notebook.add(myFrame3, text='Plating')
my_notebook.add(myFrame4, text='Material Ready')
my_notebook.add(myFrame5, text='Total')




#___________________________________ENTRYFRAME FRAME1_____________________________________
# Creating dropbox
material_name_list= ['Material 1', 'Material 2', 'Material 3', 'Material 4', 'Material 5', 'Material 6', 'Material 7', 'Material 8', 'Material 9', 'Material 10', 'Material 11', 'Material 12', 'Material 13', 'Material 14', 'Material 15', 'Material 16', 'Material 17', 'Material 18', 'Material 19', 'Material 20', 'Material 21', 'Material 22', 'Material 23', 'Material 24', 'Material 25', 'Material 26', 'Material 27', 'Material 28', 'Material 29', 'Material 30', 'Material 31']
clicked = StringVar()
clicked.set('Select Material')
drop = OptionMenu(myFrame1, clicked, *material_name_list)
drop.grid(row=1,column=0)

# Creating name and weight label
label_name= Label(myFrame1, text='Name')
label_name.grid(row=0,column=0)
label_weight= Label(myFrame1, text='Weight Kg')
label_weight.grid(row=0,column=1)

# Creating input for adding weight
weight_text= StringVar()
entry_weight_material = Entry(myFrame1, textvariable=weight_text)
entry_weight_material.grid(row=1, column=1)
button_sendToProcessing = Button(myFrame1, text= 'Send to Processing', command= send_to_processing)
button_sendToProcessing.grid(row=1, column=3)



# ____________________________________PROCESSING FRAME 2___________________________________________________________
#Processing Frame
button_processing_viewall= Button(myFrame2, text='View all', command=view_command_processing).grid(row=3,column=0)
button_processing_toPlating= Button(myFrame2, text="Send to Plating", command= send_to_plating).grid(row=3,column=1)

label_processing = Label(myFrame2, text="Selected").grid(row=0, column=0)
label_kg_processing= Label(myFrame2,text='Kg').grid(row=0,column=2)

weight_to_plat = StringVar()
name_to_plat = StringVar()
entry_processing= Entry(myFrame2,textvariable=weight_to_plat)
entry_processing.grid(row=0, column=1)
entry_processing_name = Entry(myFrame2, width = 25,textvariable=name_to_plat)
entry_processing_name.grid(row=1, column=0, columnspan=2)
entry_processing_weight = Entry(myFrame2)
entry_processing_weight.grid(row=2, column=0)
entry_processing_number = Entry(myFrame2)
entry_processing_number.grid(row=2, column=1)

list_processing= Listbox(myFrame2, font = "Helvetica", activestyle = 'dotbox', highlightcolor= 'red',bd = 5, height=20, width=70)
list_processing.grid(row=3,column=3, rowspan=2)
list_processing.bind('<<ListboxSelect>>',get_selected_row_process)

# ____________________________________PLATING FRAME 3___________________________________________________________

#Plating Frame

button_plating_viewall= Button(myFrame3, text='View all', command= view_command_plating).grid(row=3,column=0)
button_plating_toPack= Button(myFrame3, text="Got from Plating", command=send_to_toPack).grid(row=3,column=1)

label_plating = Label(myFrame3, text="Selected").grid(row=0, column=0)
label_kg_plating = Label(myFrame3,text='Kg').grid(row=0,column=2)

name_to_topack=StringVar()
weight_to_topack= StringVar()
entry_plating= Entry(myFrame3, textvariable=weight_to_topack)
entry_plating.grid(row=0, column=1)
entry_plating_name = Entry(myFrame3, width = 25, textvariable=name_to_topack)
entry_plating_name.grid(row=1, column=0, columnspan=2)

entry_plating_weight = Entry(myFrame3)
entry_plating_weight.grid(row=2, column=0)
entry_plating_number = Entry(myFrame3)
entry_plating_number.grid(row=2, column=1)

list_plating=Listbox(myFrame3, font = "Helvetica", activestyle = 'dotbox', highlightcolor= 'red',bd = 5, height=20, width=70)
list_plating.grid(row=3,column=3, rowspan=2)
list_plating.bind('<<ListboxSelect>>',get_selected_row_plating)


#___________________________MATERIAL READY FRAME 4______________________________________________________________


button_toPack_viewall= Button(myFrame4, text='View all', command= view_command_toPack).grid(row=3,column=0)
button_toPack_Packed= Button(myFrame4, text="Send to Company", command= send_to_company ).grid(row=3,column=1)

label_toPack = Label(myFrame4, text="Selected").grid(row=0, column=0)
label_kg_toPack = Label(myFrame4,text='Number', ).grid(row=0,column=2)

name_to_pack=StringVar()
weight_to_pack= StringVar()

entry_toPack= Entry(myFrame4, textvariable=weight_to_pack).grid(row=0, column=1)
entry_toPack_name = Entry(myFrame4, width = 25, textvariable=name_to_pack)
entry_toPack_name.grid(row=1, column=0, columnspan=2)
entry_toPack_weight = Entry(myFrame4)
entry_toPack_weight.grid(row=2, column=0)
entry_toPack_number = Entry(myFrame4)
entry_toPack_number.grid(row=2, column=1)


list_toPack=Listbox(myFrame4, font = "Helvetica", activestyle = 'dotbox', highlightcolor= 'red',bd = 5, height=20, width=70)
list_toPack.grid(row=3,column=3, rowspan=2)
list_toPack.bind('<<ListboxSelect>>',get_selected_row_topack)



#___________________________PACKED FRAME 5______________________________________________________________
def get_selected_row_total(event):
    try:
        global selected_tuple_5
        index = list_total.curselection()[0]
        selected_tuple_5 = list_total.get(index)
        t_label_name.delete(0,END)
        t_label_name.insert(END,selected_tuple_5[0])
        t_label_weight.delete(0, END)
        t_label_weight.insert(END,selected_tuple_5[1])
        t_label_number.delete(0, END)
        t_label_number.insert(END,selected_tuple_5[2])
    except IndexError:
        pass

#Total Frame
button_total = Button(myFrame5, text= 'View Total', command= total_view)
button_total.grid(row=0,column=0)

t_label_name = Entry(myFrame5)
t_label_name.grid(row=0,column=1)

t_label_weight = Entry(myFrame5)
t_label_weight.grid(row=0,column=1, rowspan=2)

t_label_number = Entry(myFrame5)
t_label_number.grid(row=0,column=2, rowspan=2)


list_total=Listbox(myFrame5, height=50, width=70, font = "Helvetica", activestyle = 'dotbox', highlightcolor= 'red',bd = 5)
list_total.grid(row=1,column=0, rowspan=2)


list_total.bind('<<ListboxSelect>>',get_selected_row_total)

root.mainloop()