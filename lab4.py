class university:
    def __init__(self):
        self.name=None
        self.age=None
        self.marks=None
    def input(self):
        self.name=input("Enter name:")
        self.age=int(input("Enter age:"))
        self.marks=int(input("Enter marks:"))
    def validate_marks(self,marks):
        if(self.marks>=0 and self.marks<=100):
            return True
        return False
    def validate_age(self,age):
        if(self.age>20):
            return True
        return False
    def check_qualification(self,age,marks):
        if(self.validate_age(age)==True and self.validate_marks(marks)==True):
            if(marks>65):
                return True
            return False
        return False
s=university()
s.input()
temp=s.check_qualification(s.age,s.marks)
if(temp==True):
    print("congrats")
else:
    print("Invalid input rejected")
        
"""output
>>> 
======================== RESTART: /home/bmsce/lab4.py ========================
Enter name:sumukh
Enter age:25
Enter marks:98
congrats
>>> 
======================== RESTART: /home/bmsce/lab4.py ========================
Enter name:virat
Enter age:12
Enter marks:65
Invalid input rejected
>>> 
======================== RESTART: /home/bmsce/lab4.py ========================
Enter name:rohit
Enter age:32
Enter marks:50
Invalid input rejected
"""

