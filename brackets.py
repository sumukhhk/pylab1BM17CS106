class Brackets:

    def __init__(self):
        self.inp=''

    def get(self):
        self.inp=input('\nEnter string : ') 
    
    def check(self):
        x=self.inp
        s=[]
        openB=['(','{','[']
        closeB=[')','}',']']
        for i in x:
            if i in openB:
                s.append(i)
            elif i in closeB:
                if len(s)>0:
                    k=closeB.index(i)
                    if s.pop()!=openB[k]:
                        return False
                else:
                    return False
        if len(s)>0:
            return False
        return True

    def disp(self):
        res=self.check()
        if res==True:
            print('Valid')
        else:
            print('Invalid')


a=Brackets()
a.get()
a.disp()

'''OUTPUT
Enter string : {()}
Valid

Enter string : []{]
Invalid
'''
