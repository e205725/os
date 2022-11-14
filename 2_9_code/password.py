import string
import secrets

def password(size=12):
   chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

   return ''.join(secrets.choice(chars) for x in range(size))

for i in range(10):
   print(password(10))
