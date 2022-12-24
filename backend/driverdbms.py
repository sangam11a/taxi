from backend.connection import connect
import sys

def updatedriverstatus(did):
    sql = """UPDATE driver SET status=%s WHERE driver_id=%s"""
    values = (did.getStatus(), did.getDriver_id())
    updatedriverstatusresult=False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        updatedriverstatusresult = True
    except:
        print("Error :", sys.exc_info())
    finally:
        del values, sql
        return updatedriverstatusresult

def driverontable():
    sql ="""SELECT * FROM driver"""
    tabledriver=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        tabledriver=cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error :", sys.exc_info())
    finally:
        del sql
        return tabledriver

def adminadddriver(driverInfo):
    sql ="""INSERT INTO driver VALUES(%s,%s,%s,%s,%s,%s,%s)"""
    values = (driverInfo.getDriver_id(), driverInfo.getFullname(), driverInfo.getAddress(), driverInfo.getEmail(),
              driverInfo.getLicenseno(), driverInfo.getStatus(), driverInfo.getPassword())
    result=False
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result=True
    except:
        print("Error :", sys.exc_info())
    finally:
        del values, sql
        return result


def availabledrivers():
    sql ="""SELECT driver_id FROM driver where status='Active'"""
    driver=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        driver=cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error :", sys.exc_info())
    finally:
        del sql
        return driver