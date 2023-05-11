import sqlite3
from tkinter import *
from tkinter import messagebox
import subprocess
import os
root = Tk()
root.attributes('-fullscreen', True)

root.title(" Pharmacy Managment System(manger)")
root.configure(width=1500,height=600,bg='orange')
def create_table():
    conn=sqlite3.connect("dat.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mangerDB (name TEXT, PASSWORD TEXT , ID TEXT)")
    conn.commit()
    conn.close()
def home():
    script_path = os.path.join(os.path.dirname(__file__), 'main.py')
    subprocess.run(['python', script_path])
    root.destroy()  # Close the window when the button is clicked

def addMANGER():
    create_table()
    e1= entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    conn=sqlite3.connect("dat.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO mangerDB VALUES (?,?,?)",(e1,e2,e3))
    conn.commit()
    conn.close()
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)




    
def deleteMANGER():
    e1=entry1.get()
    conn=sqlite3.connect("dat.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM mangerDB WHERE name=?",(e1,))
    conn.commit()
    conn.close()
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)



    conn.close()
def updateMANGER():
    
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    conn=sqlite3.connect("dat.db")
    cur=conn.cursor()
    cur.execute("UPDATE mangerDB SET PASSWORD=?, ID=? WHERE name=?",(e2,e3,e1))
    conn.commit()
    conn.close()

 











def searchMANGER():
    conn=sqlite3.connect("dat.db")
    e11 = entry1.get()
    cur=conn.cursor()
    cur.execute("SELECT * FROM mangerDB")
    rows=cur.fetchall()
    conn.commit()
    output=rows
    for i in output:
        if e11 in i:
            v=i
    
    try:
        
       
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry1.insert(END, str(v[0]))
        entry2.insert(END, str(v[1]))
        entry3.insert(END, str(v[2]))
    except:
         
        messagebox.showinfo("Title", "not found")
        working.close()


def clearMANGER():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
label0= Label(root,text="MANGER SERVICES  ",bg="orange",fg="white",font=("Times", 30))
label1=Label(root,text="ENTER MANGER NAME",bg="orange",relief="ridge",fg="white",font=("Times", 12),width=25)
entry1=Entry(root , font=("Times", 12))
label2=Label(root, text="ENTER MANGER ID",bd="2",relief="ridge",bg="orange",fg="white", font=("Times", 12),width=25)
entry2= Entry(root, font=("Times", 12))
label3=Label(root, text="ENTER MANGER PASSWORD",bg="orange",relief="ridge",fg="white", font=("Times", 12),width=25)
entry3= Entry(root, font=("Times", 12))
label00=Label(root, text=" SEARCH OR DELETE BY name ",bg="orange",relief="ridge",fg="white", font=("Times", 12),width=30)

button1= Button(root, text="ADD MANGER", bg="white", fg="black", width=25, font=("Times", 12),command=addMANGER)
button2= Button(root, text="DELETE MANGER", bg="white", fg="black", width =25, font=("Times", 12),command=deleteMANGER)
button3= Button(root, text="UPDATE MANGER", bg="white", fg="black", width =25, font=("Times", 12),command=updateMANGER)
button4= Button(root, text="SEARCH MANGER", bg="white", fg="black", width =25, font=("Times", 12),command=searchMANGER)
button6=Button(root,text='Close', bg="white", fg="black", width=25, font=("Times", 12),command=root.destroy)
button5= Button(root, text="CLEAR SCREEN", bg="white", fg="black", width=25, font=("Times", 12),command=clearMANGER)
button7= Button(root, text="Home", bg="white", fg="black", width=25, font=("Times", 12),command=home)

label0.grid(columnspan=6, padx=10, pady=10)
label1.grid(row=1,column=0, sticky=W, padx=10, pady=10)
label2.grid(row=2,column=0, sticky=W, padx=10, pady=10)
label3.grid(row=3,column=0, sticky=W, padx=10, pady=10)
label00.grid(row=4,column=0, sticky=W, padx=10, pady=10)                
entry1.grid(row=1,column=1, padx=40, pady=10)
entry2.grid(row=2,column=1, padx=10, pady=10)
entry3.grid(row=3,column=1, padx=10, pady=10)
button1.grid(row=1,column=4, padx=40, pady=10)
button2.grid(row=1,column=5, padx=40, pady=10)
button3.grid(row=2,column=4, padx=40, pady=10)
button4.grid(row=2,column=5, padx=40, pady=10)
button5.grid(row=3,column=4, padx=40, pady=10)
button6.grid(row=3,column=5, padx=40, pady=10)
button7.grid(row=7,column=1, sticky=W, padx=10, pady=10)






root.mainloop()

