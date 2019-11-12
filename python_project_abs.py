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
    item_id=input("Enter the item to retreive the item details")
    cursor.execute("SELECT * FROM ITEM_LIST WHERE ITEM_ID=?",(item_id,))
    r=cursor.fetchone()
    if(r!=None):
        for row in r:            
              print("ITEM_ID=",row[0])
              print("ITEM_NAME=",row[1])
              print("ITEM_COST=",row[2])
              print("ITEM_QTY=",row[3],"\n")
    else:
        print("Not found!")
      
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
    cur.execute("INSERT INTO CUSTOMER VALUES(?,?,?,?)",(cus_id,cus_name,cus_mob,balance))

def Display_customer():
    cursor.execute("SELECT * from CUSTOMER")
    rows=cursor.fetchall()
    for row in rows:
        print(row)

def retreive_customer():
    cus_id=input("Enter the customer id of the customer to dispaly")
    cursor.execute("SELECT * from CUSTOMER WHERE CUS_ID=?",(cus_id,))
    row=cur.fetchone()
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
