def searchlist(a,n,key):
    f=0
    beg=0
    end=n-1
    while(beg<=end):
        mid=int((beg+end)/2)
        if(a[mid]==key):
            f=1
            break
        elif (a[mid]<key):
            beg=mid+1
        else:
            end=mid-1
    if(f==1):
        print("element found")
    else:
        print("element not found")
lst=[]
size=int(input("Enter size of the list"))
print("Enter elements:(in order)")
for i in range(size):
    x=int(input())
    lst.append(x)
ele=int(input("Enter element to be searched:"))
searchlist(lst,size,ele)
