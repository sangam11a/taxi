import sys
from backend.connection import connect


def customerlogin(z):
    sql="""SELECT * FROM customer WHERE cus_username=%s AND cus_password=%s"""
    values=(z.getCus_username(),z.getCus_password())
    record1=None
    try:
        conn= connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        record1 = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("error",sys.exc_info())
    finally:
        del values,sql
        return record1

def driverlogin(z):
    sql="""SELECT * FROM driver WHERE email=%s AND password=%s"""
    values=(z.getEmail(),z.getPassword())
    record2=None
    try:
        conn= connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        record2 = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("error",sys.exc_info())
    finally:
        del values,sql
        return record2

def adminlogin(z):
    sql="""SELECT * FROM admin WHERE email=%s AND password=%s"""
    values=(z.getEmail(),z.getPassword())
    record3=None
    try:
        conn= connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        record3 = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("error",sys.exc_info())
    finally:
        del values,sql
        return record3