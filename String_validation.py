import re

regex_mail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex_name = '^/S[A-Za-z/d]+/S'
regex_password = ''
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


