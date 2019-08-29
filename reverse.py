def func(str1):
    s=""
    for i in str1:
        s=i+s
    print(s)

def func1(str1):
    s=str1.split(" ")
    s1=s[::-1]
    output=' '.join(s1)
    return output
str1="Welcome to BMSCE"
print("Input String: ",str1)
t=func1(str1)
func(t)
print(t)
