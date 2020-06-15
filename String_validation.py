import re

regex_mail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex_name = '^[a-zA-z0-9_-]{3,15}$'
regex_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
#STRING CONDTION WHILE INPUT
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

