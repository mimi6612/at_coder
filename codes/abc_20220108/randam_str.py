import random
import string


def randam_string(n):
    randlst = [random.choice(string.ascii_letters + string.digits)
               for i in range(n)]
    return ''.join(randlst)


print(randam_string(5000))
