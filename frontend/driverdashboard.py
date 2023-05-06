from tkinter import *
from tkinter import ttk, messagebox

from PIL import ImageTk, Image

from backend.bookingDBMS import driver_bookingtable, updatebookingstatus
from backend.driverdbms import updatedriverstatus
from frontend import Login
from middleware.driver import Driver
from middleware import Global
from middleware.booking import Booking


class DriverDashboard():
    def __init__(self,root):
        self.root=root
        self.root.geometry("600x600")
        self.root.title("Driver Dashboard")
        self.root.config(background="alice blue")
        self.root.state("zoomed")

        tableframe= Frame(root, bg="ghost white", height=70)
        tableframe.pack(side=TOP, fill=BOTH)

        def logout():
            self.root.destroy()
            win=Tk()
            Login.login(win)
            win.mainloop()

        Logout= Button(tableframe, text="Logout", bg="ghost white", bd=0, font=('Verdana', 18), command=logout)
        Logout.place(x=1150, y=10)


        image = Image.open('../frontend/group.png')
        image = image.resize((90, 80), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        Image_Label = Label(tableframe, image=image)
        Image_Label.image = image
        Image_Label.place(x=10, y=0)

        mainframe= Frame(root, bg="alice blue")
        mainframe.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

        didtxt = Entry(mainframe)
        didtxt.insert(0, Global.currentdriver[0])

        bidtxt = Entry(mainframe)


        customernamelbl= Label(mainframe, text="Customer Name", bg="alice blue", bd=0, font=('Verdana', 14))
        customernamelbl.place(x=50, y=60)

        Pickupaddresslbl= Label(mainframe, text='Pickup Address', bg="alice blue", bd=0, font=('Verdana', 14))
        Pickupaddresslbl.place(x=300, y=60)

        pickuptimelbl= Label(mainframe, text="Pickup Time", bg="alice blue", bd=0, font=('Verdana', 14))
        pickuptimelbl.place(x=550, y=60)

        customernamefield= Entry(mainframe, font=('Verdana', 12))
        customernamefield.place(x=50, y=90)

        pickupaddressfield= Entry(mainframe, font=('Verdana', 12))
        pickupaddressfield.place(x=300, y=90)

        pickuptimefield= Entry(mainframe, font=('Verdana', 12))
        pickuptimefield.place(x=550, y=90)

        pickupdatelbl= Label(mainframe, text="Pickup Date", bg="alice blue", bd=0, font=('Verdana', 14))
        pickupdatelbl.place(x=50, y=160)

        pickupdatefield= Entry(mainframe, font=('Verdana', 12))
        pickupdatefield.place(x=50, y=190)

        dropaddresslbl = Label(mainframe, text='Drop Address', bg='alice blue', bd=0, font=('Verdana', 14))
        dropaddresslbl.place(x=300,y=160)

        dropaddressfield = Entry(mainframe, font=('Verdana', 12))
        dropaddressfield.place(x=300, y=190)

        def updatebydriver():
            if bidtxt.get()=='':
                messagebox.showerror('TBS','Please Fill The Field')
            else:
                result12 = Booking(status='Completed', booking_id=bidtxt.get())
                updatebookingstatusresult=updatebookingstatus(result12)
                updatebookingresult = Driver(driver_id=didtxt.get(), status='Active')
                updatedriverstatusresult=updatedriverstatus(updatebookingresult)
                if updatebookingstatusresult==True:
                    messagebox.showinfo("Taxi Booking","Trip Completed")
                    treeview.delete(*treeview.get_children())
                    driverbookingtable()
                else:
                    messagebox.showerror("Taxi Booking","Error Occurred!")

        completebtn = Button(mainframe, text='Complete', bg='alice blue', bd=3, font=('Verdana', 12), command=updatebydriver)
        completebtn.place(x=550, y=170)

        def clearfunction():
            bidtxt.delete(0, END)
            customernamefield.delete(0, END)
            pickupaddressfield.delete(0, END)
            dropaddressfield.delete(0, END)
            pickupdatefield.delete(0, END)
            pickuptimefield.delete(0, END)

        clearbtn = Button(mainframe, text=' Clear ', bg='alice blue', bd=3, font=('Verdana', 12), command=clearfunction)
        clearbtn.place(x=700, y=170)

        treeview = ttk.Treeview(mainframe, height=16)
        treeview['columns']=('bid', 'customername', 'phonenumber', 'pickupaddress', 'dropaddress', 'pickupdate','pickuptime', 'status')
        treeview.column("#0", width=0, stretch=0)
        treeview.column('bid', width=0, stretch=0)
        treeview.column('customername', width=80, anchor=CENTER)
        treeview.column('phonenumber', width=80, anchor=CENTER)
        treeview.column('pickupaddress', width=80, anchor=CENTER)
        treeview.column('dropaddress', width=80, anchor=CENTER)
        treeview.column('pickupdate', width=80, anchor=CENTER)
        treeview.column('pickuptime', width=80, anchor=CENTER)
        treeview.column('status', width=80, anchor=CENTER)

        treeview.heading('#0', text='', anchor=CENTER)
        treeview.heading('bid', text='', anchor=CENTER)
        treeview.heading('customername', text='Customer Name', anchor=CENTER)
        treeview.heading('phonenumber', text='Phone Number', anchor=CENTER)
        treeview.heading('pickupaddress', text='Pickup Address', anchor=CENTER)
        treeview.heading('dropaddress', text='Drop Address', anchor=CENTER)
        treeview.heading('pickupdate', text='Pickup Date', anchor=CENTER)
        treeview.heading('pickuptime', text='Pickup Time', anchor=CENTER)
        treeview.heading('status', text='Status', anchor=CENTER)
        treeview.pack(side=BOTTOM, fill=BOTH)

        def driverbookingtable():
            result = driver_bookingtable(didtxt.get())
            for x in result:
                treeview.insert(parent='', index='end', values=(x[0],x[1], x[2], x[3], x[4], x[5], x[6], x[7]))
        driverbookingtable()

        def getdatafromtable(a):
            bidtxt.delete(0, END)
            customernamefield.delete(0, END)
            pickupaddressfield.delete(0, END)
            dropaddressfield.delete(0, END)
            pickupdatefield.delete(0, END)
            pickuptimefield.delete(0, END)

            selectitem = treeview.selection()[0]
            bidtxt.insert(0, treeview.item(selectitem)['values'][0])
            customernamefield.insert(0, treeview.item(selectitem)['values'][1])
            pickupaddressfield.insert(0, treeview.item(selectitem)['values'][2])
            dropaddressfield.insert(0, treeview.item(selectitem)['values'][3])
            pickupdatefield.insert(0, treeview.item(selectitem)['values'][4])
            pickuptimefield.insert(0, treeview.item(selectitem)['values'][5])

        treeview.bind('<<TreeviewSelect>>', getdatafromtable)


if __name__ == '__main__':
    root = Tk()
    DriverDashboard(root)
    root.mainloop()

