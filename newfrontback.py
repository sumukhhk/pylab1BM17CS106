#----------------------------------BACKEND-----------------------------#

import sqlite3
conn=sqlite3.connect('test.db')
print("Connection established...")
cursor=conn.cursor()

#---------------------ITEM_TABLE---------------------------------#

cursor.execute('''CREATE TABLE IF NOT EXISTS ITEM_LIST(
                ITEM_ID TEXT PRIMARY KEY,
                ITEM_NAME TEXT NOT NULL,
                ITEM_COST FLOAT NOT NULL,
                ITEM_QTY INT NOT NULL);''')
conn.commit()
def insert_item():
    item_id=input("Enter item id")
    item_name=input("Enter item name")
    item_cost=float(input("Enter cost of the item"))
    item_qty=int(input("Enter quantity"))
    cursor.execute("INSERT INTO ITEM_LIST(ITEM_ID,ITEM_NAME,ITEM_COST,ITEM_QTY)VALUES(?,?,?,?)",(item_id,item_name,item_cost,item_qty))
    conn.commit()
    print("Insertion done")
            
def display_item():
    cursor=conn.execute("SELECT * FROM ITEM_LIST")
    for row in cursor:
      print("ITEM_ID=",row[0])
      print("ITEM_NAME=",row[1])
      print("ITEM_COST=",row[2])
      print("ITEM_QTY=",row[3],"\n")

def retreive_item():
    item_id=input("Enter the item id of the item to dispaly")
    cursor.execute("SELECT * from ITEM_LIST WHERE ITEM_ID=?",(item_id,))
    row=cursor.fetchone()
    print(row)

      
def update_item():    
    item_id=input("Enter item id")
    item_name=input("Enter item name")
    item_cost=float(input("Enter item cost"))
    item_qty=input("Enter quantity")
    cursor.execute("UPDATE ITEM_LIST SET ITEM_NAME=?,ITEM_COST=?,ITEM_QTY=? WHERE ITEM_ID=?",(item_name,item_cost,item_qty,item_id))
    print("Update done")
    conn.commit()

def delete_item():
    item_id=input("Enter the item id to delete the item details")
    cursor.execute("DELETE FROM ITEM_LIST WHERE ITEM_ID=?",(item_id,))
    conn.commit()
    print("Record successfully deleted")   

#------------------------CUSTOMER TABLE-------------------------------------#
    
cursor.execute('''CREATE TABLE IF NOT EXISTS CUSTOMER(
                CUS_ID TEXT PRIMARY KEY,
                CUS_NAME TEXT NOT NULL,
                CUS_MOB LONG NOT NULL,
                BALANCE FLOAT NOT NULL);''')
conn.commit()

def Insert_customer():
    cus_id=input("\nEnter Customer id: ")
    cus_name=input("\nEnter Name: ")
    cus_mob=int(input("\nEnter mobile number: "))
    balance=int(input("Enter amount in the card"))
    cursor.execute("INSERT INTO CUSTOMER(CUS_ID,CUS_NAME,CUS_MOB,BALANCE) VALUES(?,?,?,?)",(cus_id,cus_name,cus_mob,balance))
    conn.commit()
    print("Insertion Done")

def Display_customer():
    cursor.execute("SELECT * from CUSTOMER")
    rows=cursor.fetchall()
    for row in rows:
        print(row)

def retreive_customer():
    cus_id=input("Enter the customer id of the customer to dispaly")
    cursor.execute("SELECT * from CUSTOMER WHERE CUS_ID=?",(cus_id,))
    row=cursor.fetchone()
    print(row)

def update_customer():    
    cus_id=input("Enter customer id")
    cus_name=input("Enter item name")
    cus_mob=int(input("Enter customer mobile number"))
    cursor.execute("UPDATE ITEM_LIST SET CUS_NAME=?,CUS_MOB=? WHERE CUS_ID=?",(cus_name,cus_mob,cus_id))
    print("Update done successfully!!!")
    conn.commit()

def update_balance():
    cus_id=input("Enter customer id to update balance")
    cursor.execute("UPDATE ITEM_LIST SET BALANCE=? WHERE CUS_ID=?",(BALANCE,cus_id))
    print("Balance successfully updated!!!")
    conn.commit()                   

def delete_customer():
    cus_id=input("Enter the customerid to delete the customer details")
    cursor.execute("DELETE FROM CUSTOMER WHERE CUS_ID=?",(cus_id,))
    conn.commit()
    print("Record successfully deleted")


#---------------------------FRONTEND-------------------------


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
def main_account_screen():
    global main_screen
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("300x250") # set the configuration of GUI window 
    main_screen.title("XYZ Super Market") # set the title of GUI window
    
    
    #login_screen.geometry("300x250")
    Label(main_screen, text="Please enter details below to login").pack()
    Label(main_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()
    Label(main_screen, text="Username  ").pack()
    username_login_entry = Entry(main_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(main_screen, text="").pack()
    Label(main_screen, text="Password  ").pack()
    password__login_entry = Entry(main_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Login", width=10, height=1, command=verify).pack()
    main_screen.mainloop()
def verify():
    #print(username_verify.get(), password_verify.get())
    if(username_verify.get()=="hello" and password_verify.get()=="world"):
        home_page()
    else:
        messagebox.showinfo("Title","invalid usewrname/password")
def home_page():
    main_screen.withdraw()
    global screen
    screen=Toplevel(main_screen)
    screen.geometry("300x250")
    Label(screen, text="Home Page").pack()
    Label(screen, text="").pack()
    Button(screen, text="ITEM",width=20, height=3,bd=10,command=item_page ).pack()
    Button(screen, text="CUSTOMER", width=20, height=3,bd=10,command=customer_page).pack()
    Button(screen, text="LOG OUT", width=10,height=1,command=main_logout).pack()
def main_logout():
    #main_screen.withdraw()
    screen.withdraw()
    main_screen.iconify()
def item_page():
    screen.withdraw()
    global item_screen
    item_screen=Toplevel(main_screen)
    item_screen.geometry("500x500")
    Label(item_screen, text="Item Page").pack()
    Button(item_screen, text="INSERT",width=20, height=3,bd=10,command=insert_item).pack()
    Button(item_screen, text="UPDATE",width=20, height=3,bd=10,command=update_item).pack()
    Button(item_screen, text="DISPLAY",width=20, height=3,bd=10,command=retreive_item).pack()
    Button(item_screen, text="DELETE",width=20, height=3,bd=10,command=delete_item).pack()
    Button(item_screen, text="DISPLAY ALL",width=20, height=3,bd=10,command=display_item).pack()
    Button(item_screen, text="Back",width=10,height=2,command=back_item).pack()
def back_item():
    item_screen.withdraw()
    home_page()
def customer_page():
    screen.withdraw()
    global cus_screen
    cus_screen=Toplevel(main_screen)
    cus_screen.geometry("500x500")
    Label(cus_screen, text="Customer Page").pack()
    Button(cus_screen, text="INSERT",width=20, height=3,bd=10,command=Insert_customer).pack()
    Button(cus_screen, text="UPDATE",width=20, height=3,bd=10,command=update_customer).pack()
    Button(cus_screen, text="DISPLAY",width=20, height=3,bd=10,command=retreive_customer).pack()
    Button(cus_screen, text="DELETE",width=20, height=3,bd=10,command=delete_customer).pack()
    Button(cus_screen, text="DISPLAY ALL",width=20, height=3,bd=10,command=Display_customer).pack()
    Button(cus_screen, text="Back",width=10,height=2,command=back_cus).pack()
def back_cus():
    cus_screen.withdraw()
    home_page()
main_account_screen()


