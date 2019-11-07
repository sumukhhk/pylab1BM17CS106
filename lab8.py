import sqlite3
conn=sqlite3.connect('test.db')
print("Connection established...")
conn.execute('''CREATE TABLE IF NOT EXISTS STUDENT_106(
                NAME CHAR(30) NOT NULL,
                USN CHAR(20) PRIMARY KEY,
                SEM INT,
                BRANCH CHAR(10));''')
conn.commit()
def insert():
    NAME=input("Enter name")
    USN=input("Enter usn")
    SEM=int(input("Enter semester"))
    BRANCH=input("Enter branch")
    conn.execute("INSERT INTO STUDENT_106(NAME,USN,SEM,BRANCH)VALUES(?,?,?,?)",(NAME,USN,SEM,BRANCH))
    conn.commit()
    print("Insertion done")
            
def display():
    cursor=conn.execute("SELECT NAME,USN,SEM,BRANCH FROM STUDENT_106")
    for row in cursor:
      print("NAME=",row[0])
      print("USN=",row[1])
      print("SEM=",row[2])
      print("BRANCH=",row[3],"\n")

def retreive():
    USN=input("Enter the usn to retreive the student details")
    cursor=conn.execute("SELECT * FROM STUDENT_106 WHERE USN=?",(USN,))
    r=cursor.fetchall()
    if(r!=None):
        for row in r:            
              print("NAME=",row[0])
              print("USN=",row[1])
              print("SEM=",row[2])
              print("BRANCH=",row[3],"\n")
                    
    else:
        print("Not found!")
      
def update():
    NAME=input("Enter name")
    USN=input("Enter usn")
    SEM=int(input("Enter semester"))
    BRANCH=input("Enter branch")
    conn.execute("UPDATE STUDENT_106 SET NAME=?,SEM=?,BRANCH=? WHERE USN=?"(NAME,SEM,BRANCH,USN))
    print("Update done")
    conn.commit()

def delete():
    USN=input("Enter the usn to delete the student details")
    conn.execute("DELETE FROM STUDENT_106 WHERE USN=?",(USN,))
    conn.commit()
    print("Record successfully deleted")   

c=-1
while(c!=0):
    print("Enter:","\n","1:insert ","\n","2:dispaly_all","\n","3:display_specific","\n","4:delete","\n","5:update","\n","0:exit","\n")
    c=int(input("Enter your choice"))
    if(c==1):
        n=int(input("Enter the number of students you want to insert"))
        for i in range(n):
            insert()
    elif(c==2):
        display()
    elif(c==3):
        retreive()
    elif(c==4):
        delete()
    elif(c==5):
        update()
    elif(c==0):
        break
    else:
        print("Please enter a valid number")
conn.close()
