import pyodbc
from binary_search import Binarysearch

conn = pyodbc.connect(DSN='kivy_storage',autocommit=True)
cursor = conn.cursor()
name_validation = [n[0] for n in cursor.execute('select username from singup')]
email_validation = [e[0] for e in cursor.execute('select email from singup')]
password_validation = [p[0] for p in cursor.execute('select password from singup')]
userid_validation = [u[0] for u in cursor.execute('select userid from singup')]
user_validation = [u for u in cursor.execute('select username,password from singup')]
uid = len(user_validation)+101


def singin_validator(name,password):
    cursor.execute('truncate table singupdummy')
    v = (name, password)
    cursor.execute('insert into singupdummy values(?,?)', f'{v[0]}', f'{v[1]}')
    val = [v for v in cursor.execute('select username,password from singupdummy')]
    try:
        return userid_validation[user_validation.index(val[-1])]
    except  ValueError:
        return 'invalid'

    
