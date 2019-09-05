import random
import string
s1=random.choice(string.ascii_lowercase)
s2=random.choice(string.ascii_uppercase)
s3=random.choice(string.punctuation)
s4=random.choice(string.digits)
letters=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
len=random.randint(4,16)
password=s1+s2+s3+s4+''.join(random.sample(letters,l))
p=''.join(random.sample(password,l+4))
print(p)
