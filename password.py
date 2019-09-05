import random
import string
s1=random.choice(string.ascii_lowercase)
s2=random.choice(string.ascii_uppercase)
s3=random.choice(string.punctuation)
s4=random.choice(string.digits)
letters=string.ascii_lowercase+string.ascii_lowercase+string.digits+string.punctuation
password=s1+s2+s3+s4+''.join(random.sample(letters,8))
p=''.join(random.sample(password,12))
print(p)
