import mysql.connector
import sys
from backend.connection import connect

def saveBooking(bookingInfo):
    sql="""INSERT INTO booking VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
    values=(bookingInfo.getBooking_id(), bookingInfo.getPickup_address(), bookingInfo.getDropoff_address(),
            bookingInfo.getPickup_date(), bookingInfo.getPickup_time(), bookingInfo.getStatus(),
            bookingInfo.getCid(), bookingInfo.getDid())
    result=False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return result

def customertabledata(book):
    sql = """SELECT booking_id, pickup_address, dropoff_address, pickup_date, pickup_time FROM booking WHERE cid=%s AND status=%s"""
    values=(book.getCid(), book.getStatus())
    customerdata = None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        customerdata=cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error :", sys.exc_info())
    finally:
        del values, sql
        return customerdata

def cancelrequestbycus(bid):
    sql = """DELETE FROM booking WHERE booking_id=%s"""
    values = (bid,)
    cancelcustomerdata = False
    try:
        conn= connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        cancelcustomerdata=True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return cancelcustomerdata



