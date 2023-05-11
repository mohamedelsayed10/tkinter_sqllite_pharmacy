


import sqlite3
from tkinter import *
from tkinter import messagebox
import subprocess
import os
root = Tk()
root.attributes('-fullscreen', True)

root.title(" Pharmacy Managment System(LIST OF MISSING PRODUCT)")
root.configure(width=1500,height=600,bg='#856ff8')
def create_table():
    conn=sqlite3.connect("dat.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS LISTDB (name TEXT, BARCODE TEXT ,ID TEXT,QUANTITY INTGER,LOCATION TEXT)")
    conn.commit()
    conn.close()
def home():
    script_path = os.path.join(os.path.dirname(__file__), 'main.py')
    subprocess.run(['python', script_path])
    root.destroy()  # Close the window when the button is clicked


def addPRODUCT():
    create_table()
    e1= entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    conn=sqlite3.connect("dat.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO LISTDB VALUES (?,?,?,?,?)",(e1,e2,e3,e4,e5))
    conn.commit()
    conn.close()
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)



def view():
    conn=sqlite3.connect("dat.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM LISTDB")
    rows=cur.fetchall()
    conn.close()
    return rows


    
def deletePRODUCT():
    e2=entry2.get()
    conn=sqlite3.connect("dat.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM LISTDB WHERE BARCODE=?",(e2,))
    conn.commit()
    conn.close()
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)




 
def updatePRODUCT():
    
    e1=entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    conn=sqlite3.connect("dat.db")
    cur=conn.cursor()
    cur.execute("UPDATE LISTDB SET name=?, ID=?, LOCATION=?, QUANTITY=? WHERE BARCODE=?",(e1,e3,e5,e4,e2))
    conn.commit()
    conn.close()
 







def searchPRODUCT():
    conn=sqlite3.connect("dat.db")
    e11 = entry2.get()
    cur=conn.cursor()
    cur.execute("SELECT * FROM LISTDB")
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
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry1.insert(END, str(v[0]))
        entry2.insert(END, str(v[1]))
        entry3.insert(END, str(v[2]))
        entry4.insert(END, str(v[3]))
        entry5.insert(END, str(v[4]))
    except:
         
        messagebox.showinfo("Title", "error end of file")
        working.close()


def clearPRODUCT():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)


#fn1353
label0= Label(root,text="LIST OF MISSING PPRODUCT  ",bg="#856ff8",fg="white",font=("Times", 30))
label1=Label(root,text="ENTER PRODUCT NAME",bg="#856ff8",relief="ridge",fg="white",font=("Times", 12),width=25)
entry1=Entry(root , font=("Times", 12))
label2=Label(root, text="ENTER PRODUCT BARCODE",bd="2",relief="ridge",bg="#856ff8",fg="white", font=("Times", 12),width=25)
entry2= Entry(root, font=("Times", 12))
label3=Label(root, text="ENTER PRODUCT ID",bg="#856ff8",relief="ridge",fg="white", font=("Times", 12),width=25)
entry3= Entry(root, font=("Times", 12))
label4=Label(root, text="ENTER PRODUCT QUANTITY",bg="#856ff8",relief="ridge",fg="white", font=("Times", 12),width=25)
entry4= Entry(root, font=("Times", 12))
label5=Label(root, text="ENTER PRODUCT LOCATION",bg="#856ff8",relief="ridge",fg="white", font=("Times", 12),width=25)
entry5= Entry(root, font=("Times", 12))
button1= Button(root, text="ADD TO THE LIST", bg="white", fg="black", width=25, font=("Times", 12),command=addPRODUCT)
button2= Button(root, text="DELETE FROM LIST", bg="white", fg="black", width =25, font=("Times", 12),command=deletePRODUCT)
button3= Button(root, text="UPDATE PRODUCT IN LIST", bg="white", fg="black", width =25, font=("Times", 12),command=updatePRODUCT)
button4= Button(root, text="SEARCH PRODUCT IN LIST", bg="white", fg="black", width =25, font=("Times", 12),command=searchPRODUCT)
button6=Button(root,text='CLOSE', bg="white", fg="black", width=25, font=("Times", 12),command=root.destroy)
button5= Button(root, text="CLEAR SCREEN", bg="white", fg="black", width=25, font=("Times", 12),command=clearPRODUCT)
label00=Label(root, text=" SEARCH OR DELETE BY BARCODE ",bg="#856ff8",relief="ridge",fg="white", font=("Times", 12),width=25)
button7= Button(root, text="Home", bg="white", fg="black", width=25, font=("Times", 12),command=home)

label0.grid(columnspan=6, padx=10, pady=10)
label1.grid(row=1,column=0, sticky=W, padx=10, pady=10)
label2.grid(row=2,column=0, sticky=W, padx=10, pady=10)
label3.grid(row=3,column=0, sticky=W, padx=10, pady=10)
label4.grid(row=4,column=0, sticky=W, padx=10, pady=10)
label5.grid(row=5,column=0, sticky=W, padx=10, pady=10)
label00.grid(row=6,column=0, sticky=W, padx=10, pady=10)
entry1.grid(row=1,column=1, padx=40, pady=10)
entry2.grid(row=2,column=1, padx=10, pady=10)
entry3.grid(row=3,column=1, padx=10, pady=10)
entry4.grid(row=4,column=1, padx=10, pady=10)
entry5.grid(row=5,column=1, padx=10, pady=10)
button1.grid(row=1,column=4, padx=40, pady=10)
button2.grid(row=1,column=5, padx=40, pady=10)
button3.grid(row=2,column=4, padx=40, pady=10)
button4.grid(row=2,column=5, padx=40, pady=10)
button5.grid(row=3,column=4, padx=40, pady=10)
button6.grid(row=3,column=5, padx=40, pady=10)
button7.grid(row=7,column=1, sticky=W, padx=10, pady=10)



root.mainloop()






