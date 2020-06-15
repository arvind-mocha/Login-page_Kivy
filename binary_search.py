import math

def binary(arr, leastval, arrsize, sval):
    if arrsize >= leastval:
        mid = math.ceil(leastval + (arrsize - leastval) / 2)
        if arr[mid] == sval:
            return mid

        elif arr[mid] > sval:
            return binary(arr, leastval, mid - 1, sval)

        else:
            return binary(arr, mid + 1, arrsize, sval)

    else:
        return 'invalid'

import pyodbc

conn = pyodbc.connect(DSN='kivy_storage',autocommit=True)
cursor = conn.cursor()
name_validation = [n[0] for n in cursor.execute('select username from singup')]
email_validation = [e[0] for e in cursor.execute('select email from singup')]
password_validation = [p[0] for p in cursor.execute('select password from singup')]
userid_validation = [u[0] for u in cursor.execute('select userid from singup')]
user_validation = [u for u in cursor.execute('select username,password from singup')]


def Binarysearch(array,lval,size,string):
    if binary(array,lval,size,string) != 'invalid':
        validation = 'valid'
        return validation
    else:
        validation = binary(array,lval,size,string)
        return validation





