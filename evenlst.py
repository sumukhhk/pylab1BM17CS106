a=[]
b=[]
n=int(input("Enter the no of enteries in the list"))
print("Enter the list items")
for i in range(n):
    ele=int(input())
    a.append(ele)
for i in a:
    if(i%2==0):
        b.append(i)
print("The even elements in the list:")
print(b)
