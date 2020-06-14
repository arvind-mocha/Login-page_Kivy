import re

regex_mail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex_name = '^[a-zA-z0-9_-]{3,15}$'
regex_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
def checkemail(email):
    if(re.search(regex_mail,email)):
       return 'valid'
    else:
        return 'invalid'

def checkname(name):
    if(re.search(regex_name,name)):
        return 'valid'
    else:
        return 'invalid'

def checkpassword(password):
    if (re.search(regex_password, password)):
        return 'valid'

    else:
        return 'invalid'

import pyodbc

conn = pyodbc.connect(DSN='kivy_storage',autocommit=True)
cursor = conn.cursor()

name_checker = cursor.execute('select username from singup')
singup_name_checker = [c[0] for c in cursor]
print([singup_name_checker[n] for n in range(len(singup_name_checker))])