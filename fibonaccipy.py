def fib(n):
    a=0
    b=1
    c=a+b
    i=3
    if(n==1):
        print(a)
    if(n==2):
        print(a,"\n",b)
    if(n>2):
        print("The fibonacci series upto",n,"terms is:")
        print(a)
        print(b)
        print(c)
        while(i<n):
            
            a=b
            b=c
            c=a+b
            i=i+1
            print(c)
n=int(input("Enter the value of n: "))
fib(n)

"""Enter the value of n: 10
The fibonacci series upto 10 terms is:
0
1
1
2
3
5
8
13
21
34"""
