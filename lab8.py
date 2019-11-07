import sqlite3
conn=sqlite3.connect('test.db')
print("Connection established...")
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENT_106(
                NAME CHAR(30) NOT NULL,
                USN CHAR(20) PRIMARY KEY,
                SEM INT,
                BRANCH CHAR(10));''')
conn.commit()
def insert():
    name=input("Enter name")
    usn=input("Enter usn")
    sem=int(input("Enter semester"))
    branch=input("Enter branch")
    cursor.execute("INSERT INTO STUDENT_106(NAME,USN,SEM,BRANCH)VALUES(?,?,?,?)",(name,usn,sem,branch))
    conn.commit()
    print("Insertion done")
            
def display():
    cursor=conn.execute("SELECT * FROM STUDENT_106")
    for row in cursor:
      print("NAME=",row[0])
      print("USN=",row[1])
      print("SEM=",row[2])
      print("BRANCH=",row[3],"\n")

def retreive():
    usn=input("Enter the usn to retreive the student details")
    cursor.execute("SELECT * FROM STUDENT_106 WHERE USN=?",(usn,))
    r=cursor.fetchone()
    if(r!=None):
        for row in r:            
              print("NAME=",row[0])
              print("USN=",row[1])
              print("SEM=",row[2])
              print("BRANCH=",row[3],"\n")
                    
    else:
        print("Not found!")
      
def update():    
    usn=input("Enter usn")
    name=input("Enter name")
    sem=int(input("Enter semester"))
    branch=input("Enter branch")
    cursor.execute("UPDATE STUDENT_106 SET NAME=?,SEM=?,BRANCH=? WHERE USN=?",(name,sem,branch,usn))
    print("Update done")
    conn.commit()

def delete():
    usn=input("Enter the usn to delete the student details")
    cursor.execute("DELETE FROM STUDENT_106 WHERE USN=?",(usn,))
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
conn.commit()
conn.close()



'''
OUTPUT
Connection established...
Enter: 
 1:insert  
 2:dispaly_all 
 3:display_specific 
 4:delete 
 5:update 
 0:exit 

Enter your choice1
Enter the number of students you want to insert2
Enter nameSumukh
Enter usn1bm17cs106
Enter semester5
Enter branchcse
Insertion done
Enter nameshreyas
Enter usn1bm17cs098
Enter semester6
Enter branchece
Insertion done
Enter: 
 1:insert  
 2:dispaly_all 
 3:display_specific 
 4:delete 
 5:update 
 0:exit 

Enter your choice2
NAME= Sumukh
USN= 1bm17cs106
SEM= 5
BRANCH= cse 

NAME= shreyas
USN= 1bm17cs098
SEM= 6
BRANCH= ece 

Enter: 
 1:insert  
 2:dispaly_all 
 3:display_specific 
 4:delete 
 5:update 
 0:exit 

Enter your choice3
Enter the usn to retreive the student details1bm17cs106
NAME= Sumukh
USN= 1bm17cs106
SEM= 5
BRANCH= cse 

Enter: 
 1:insert  
 2:dispaly_all 
 3:display_specific 
 4:delete 
 5:update 
 0:exit 

Enter your choice4
Enter the usn to delete the student details1bm17cs098
Record successfully deleted
Enter: 
 1:insert  
 2:dispaly_all 
 3:display_specific 
 4:delete 
 5:update 
 0:exit 

Enter your choice2
NAME= Sumukh
USN= 1bm17cs106
SEM= 5
BRANCH= cse 

Enter: 
 1:insert  
 2:dispaly_all 
 3:display_specific 
 4:delete 
 5:update 
 0:exit 

Enter your choice1
Enter the number of students you want to insert1
Enter nametarun
Enter usn1bm17cs117
Enter semester3
Enter branchmech
Insertion done
Enter: 
 1:insert  
 2:dispaly_all 
 3:display_specific 
 4:delete 
 5:update 
 0:exit 

Enter your choice2
NAME= Sumukh
USN= 1bm17cs106
SEM= 5
BRANCH= cse 

NAME= tarun
USN= 1bm17cs117
SEM= 3
BRANCH= mech
Enter: 
 1:insert  
 2:dispaly_all 
 3:display_specific 
 4:delete 
 5:update 
 0:exit 

Enter your choice5
Enter usn1bm17cs117
Enter nametarunvh
Enter semester4
Enter branchise
Update done
Enter: 
 1:insert  
 2:dispaly_all 
 3:display_specific 
 4:delete 
 5:update 
 0:exit 

Enter your choice2
NAME= Sumukh
USN= 1bm17cs106
SEM= 5
BRANCH= cse 

NAME= tarunvh
USN= 1bm17cs117
SEM= 4
BRANCH= ise 

Enter: 
 1:insert  
 2:dispaly_all 
 3:display_specific 
 4:delete 
 5:update 
 0:exit 

Enter your choice0
'''

