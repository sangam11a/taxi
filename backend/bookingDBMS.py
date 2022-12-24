import mysql.connector
import sys
from backend.connection import connect

def customerbookinghistory(book):
    sql = """SELECT * FROM booking WHERE cid=%s AND NOT status='Pending'"""
    values=(book,)
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

def driver_bookingtable(did):
    sql=""" SELECT booking.booking_id, customer.cus_name, customer.cus_phone, booking.pickup_address, 
    booking.dropoff_address, booking.pickup_date, booking.pickup_time, booking.status from booking left join 
    customer on booking.cid = customer.cus_id where not booking.status='Pending' and did=%s order by booking.status desc"""
    values = (did,)
    result = None
    try:
        conn=connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        result=cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error :", sys.exc_info())
    finally:
        del sql
        return result

def updatebookingstatus(bid):
    sql =""" UPDATE booking SET status=%s WHERE booking_id=%s"""
    values=(bid.getStatus(), bid.getBooking_id())
    updatebookingstatusresult = False
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        updatebookingstatusresult=True
    except:
        print("Error :", sys.exc_info())
    finally:
        del values, sql
        return updatebookingstatusresult

def admin_bookingtable():
    sql=""" SELECT booking.booking_id, booking.cid,customer.cus_name, booking.pickup_address, 
    booking.dropoff_address, booking.pickup_date, booking.pickup_time, booking.status from booking left join 
    customer on booking.cid = customer.cus_id where booking.status='Pending'"""
    result = None
    try:
        conn=connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error :", sys.exc_info())
    finally:
        del sql
        return result

def adminupdatebooking(Info):
    sql ="""UPDATE booking SET status=%s, did=%s WHERE booking_id=%s"""
    values=(Info.getStatus(), Info.getDid(), Info.getBooking_id())
    updatebookingresult=False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        updatebookingresult = True
    except:
        print("Error :", sys.exc_info())
    finally:
        del values,sql
        return updatebookingresult