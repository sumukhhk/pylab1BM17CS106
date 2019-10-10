with open('happy.txt','r') as f:
    a=f.read()
    a=a.strip()
    a=a.split(',')

with open('prime.txt','r') as f:
    b=f.read()
    b=b.strip()
    b=b.split(',')

print("Overalapping Happy and Prime Numbers:")
for i in a:
    if i in b:
        print(i)
'''
Overalapping Happy and Prime Numbers:
 7
 13
 19
 23
 31
 79
 97
 103
 109
 139
 167
 193
 239
 263
 293
 313
 331
 367
 379
 383
 397
 409
 487
 563
 617
 653
 673
 683
 709
 739
 761
 863
 881
 907
 937'''
