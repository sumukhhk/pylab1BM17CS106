class Calldetail:
    def __init__(self,c,r,d,t):
        self.cal = c
        self.recv = r
        self.duration = d
        self.type = t
        
    def disp(self):
        print("\nCaller: ",self.cal)
        print("Receiver: ",self.recv)
        print("Duration: ",self.duration)
        print("Type: ",self.type)

class Util:
    def __init__(self):
        self.list_of_call_objects = []
        self.count = 0
        self.count1 = 0
        self.count2 = 0
    def parse_customer(self,list_of_call_string):
        for i in list_of_call_string:
            x = i.split(",")
            for j in x:
                
                if j == "ISD":
                    self.count+=1
                elif j == "Local":
                    self.count1+=1
                elif j == "STD":
                    self.count2+=1
                    
            o = Calldetail(*x)
            self.list_of_call_objects.append(o)
            
    def printdetails(self):
        for i in self.list_of_call_objects:
            i.disp()
        print("\nSTD: ", self.count)
        print("\nLocal: ", self.count1)
        print("\nISD: ",self.count2)

call1 = '9123848912,12385612934,23,STD'
call2 = '2395713534,29435812359,12,Local'
call3 = '123854295,105949324,18,ISD'
call4 = '134845,34953460,19,ISD'
list_of_call_string = [call1, call2, call3, call4]
util = Util()
util.parse_customer(list_of_call_string)
util.printdetails()


""" OUTPUT:
Caller:  9123848912
Receiver:  12385612934
Duration:  23
Type:  STD
Caller:  2395713534
Receiver:  29435812359
Duration:  12
Type:  Local
Caller:  123854295
Receiver:  105949324
Duration:  18
Type:  ISD
Caller:  134845
Receiver:  34953460
Duration:  19
Type:  ISD
STD:  2
Local:  1
ISD:  1
"""
