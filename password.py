import random
import string
letters=string.ascii_letters+string.punctuation+string.digits
len=random.randint(8,16)
password=''.join(random.sample(letters,len))
print(password)
