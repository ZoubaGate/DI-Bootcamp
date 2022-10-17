from random import *
import string
rand=''.join(choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(256))
print(rand)