import mysql.connector
import sys
from backend.connection import connect


def saveCustomer(customerInfo):

    sql = """INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s,%s)"""
    values =(customerInfo.getCus_id(), customerInfo.getCus_name(), customerInfo.getCus_address(),
            customerInfo.getCus_phone(), customerInfo.getCus_email(), customerInfo.getCus_username(),
            customerInfo.getCus_password())
    result=False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result= True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return result
