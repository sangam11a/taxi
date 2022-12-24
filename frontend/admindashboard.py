from tkinter import *
from tkinter import ttk, messagebox

from PIL import ImageTk, Image

from backend.bookingDBMS import admin_bookingtable, adminupdatebooking
from backend.driverdbms import driverontable, adminadddriver, updatedriverstatus, availabledrivers
from frontend import Login
from middleware.driver import Driver
from middleware.booking import Booking
from middleware import Global

class AdminDashboard():
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("Customer Dashboard")
        self.root.config(background="alice blue")

        font = ('Times New Roman', 16, 'normal')

        tableFrame = Frame(root, bg="ghost white", height=70)
        tableFrame.pack(side=TOP, fill=BOTH)

        def changetoassigndriver():
            assigndriverframe.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
            adddriverframe.pack_forget()

        assigndriver_btn = Button(tableFrame, text="Assign Driver", bg="ghost white", bd=0, font=('Verdana', 18), command=changetoassigndriver)
        assigndriver_btn.place(x=130, y=25)

        def changetoadddriver():
            adddriverframe.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
            assigndriverframe.pack_forget()

        adddriver_btn = Button(tableFrame,text="Add Driver", bd=0, bg="ghost white", font=('Verdana', 18), command=changetoadddriver)
        adddriver_btn.place(x=320, y=25)

        def logoutfunction():
            self.root.destroy()
            win = Tk()
            Login.login(win)
            win.mainloop()

        Logout = Button(tableFrame, command=logoutfunction, text="Logout", bg="ghost white", bd=0, font=('Verdana', 18))
        Logout.place(x=480, y=25)

        image = Image.open('../frontend/group.png')
        image = image.resize((90, 80), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        Image_Label = Label(tableFrame, image=image)
        Image_Label.image = image
        Image_Label.place(x=10, y=0)

        # assigndriver frame
        assigndriverframe = Frame(root, bg='alice blue')
        assigndriverframe.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

        # adddriver frame
        adddriverframe = Frame(root, bg='alice blue')

        # adding widgets on assign driver frame
        bookingidlbl = Label(assigndriverframe, text='Booking Id', bg="alice blue", bd=0, font=('Verdana', 14))
        bookingidlbl.place(x=50, y=60)

        Pickupaddresslbl = Label(assigndriverframe, text='Pickup Address', bg="alice blue", bd=0, font=('Verdana', 14))
        Pickupaddresslbl.place(x=300, y=60)

        pickuptimelbl = Label(assigndriverframe, text="Pickup Time", bg="alice blue", bd=0, font=('Verdana', 14))
        pickuptimelbl.place(x=550, y=60)

        bookingidfield = Entry(assigndriverframe, font=('Verdana', 12))
        bookingidfield.place(x=50, y=90)

        pickupaddressfield = Entry(assigndriverframe, font=('Verdana', 12))
        pickupaddressfield.place(x=300, y=90)

        pickuptimefield = Entry(assigndriverframe, font=('Verdana', 12))
        pickuptimefield.place(x=550, y=90)

        pickupdatelbl = Label(assigndriverframe, text="Pickup Date", bg="alice blue", bd=0, font=('Verdana', 14))
        pickupdatelbl.place(x=50, y=160)

        pickupdatefield = Entry(assigndriverframe, font=('Verdana', 12))
        pickupdatefield.place(x=50, y=190)

        dropaddresslbl = Label(assigndriverframe, text='Drop Address', bg='alice blue', bd=0, font=('Verdana', 14))
        dropaddresslbl.place(x=300, y=160)

        dropaddressfield = Entry(assigndriverframe, font=('Verdana', 12))
        dropaddressfield.place(x=300, y=190)

        assigndriverlbl = Label(assigndriverframe, text='Available Driver', bg='alice blue', bd=0, font=('Verdana', 14))
        assigndriverlbl.place(x=550, y=160)

        def driverdatas():
            driver = availabledrivers()
            data=[f for f, in driver]
            assigndriverfield.configure(values=data)
            assigndriverfield.place(x=550, y=190)

        assigndriverfield = ttk.Combobox(assigndriverframe, font=('Verdana', 12))
        driverdatas()


        def confirmbookingfunction():
            if bookingidfield.get()=='':
                messagebox.showwarning('Taxi Booking', 'Please Enter Booking Id')
            elif assigndriverfield.get()=='':
                messagebox.showwarning('Taxi Booking','Please Enter Driver ID')
            else:
                booking=Booking(booking_id=bookingidfield.get(), did=assigndriverfield.get(), status='Confirmed')
                updatebookingresult1=adminupdatebooking(booking)

                updatebookingresult = Driver(driver_id=assigndriverfield.get(), status='Inactive')
                updatedriverstatusresult = updatedriverstatus(updatebookingresult)
                if updatebookingresult1 == True:
                    messagebox.showinfo("Taxi Booking", 'The driver is assigned and booking is Confirmed')
                    treeview.delete(*treeview.get_children())
                    confirmbooking()
                    bookingidfield.delete(0, END)
                    pickupaddressfield.delete(0, END)
                    pickuptimefield.delete(0, END)
                    pickupdatefield.delete(0, END)
                    dropaddressfield.delete(0, END)
                    assigndriverfield.delete(0, END)
                    assigndriverfield.delete(0, END)
                    driverdatas()

                else:
                    messagebox.showerror('Taxi Booking', 'Error Occurred!')

        confirmbookingbtn = Button(assigndriverframe, text='Confirm Booking', bg='alice blue', font=('Verdana', 14), command=confirmbookingfunction)
        confirmbookingbtn.place(x=800, y=170)

        treeview = ttk.Treeview(assigndriverframe, height=16)
        treeview['columns'] = ('bid', 'cid','customername', 'pickupaddress', 'dropaddress', 'pickupdate', 'pickuptime', 'status')
        treeview.column("#0", width=0, stretch=0)
        treeview.column('bid', width=0, stretch=0)
        treeview.column('cid', width=80, anchor=CENTER)
        treeview.column('customername', width=80, anchor=CENTER)
        treeview.column('pickupaddress', width=80, anchor=CENTER)
        treeview.column('dropaddress', width=80, anchor=CENTER)
        treeview.column('pickupdate', width=80, anchor=CENTER)
        treeview.column('pickuptime', width=80, anchor=CENTER)
        treeview.column('status', width=80, anchor=CENTER)

        treeview.heading('#0', text='', anchor=CENTER)
        treeview.heading('bid', text='', anchor=CENTER)
        treeview.heading('cid', text='Customer Id', anchor=CENTER)
        treeview.heading('customername', text='Customer Name', anchor=CENTER)
        treeview.heading('pickupaddress', text='Pickup Address', anchor=CENTER)
        treeview.heading('dropaddress', text='Drop Address', anchor=CENTER)
        treeview.heading('pickupdate', text='Pickup Date', anchor=CENTER)
        treeview.heading('pickuptime', text='Pickup Time', anchor=CENTER)
        treeview.heading('status', text='Status', anchor=CENTER)
        treeview.pack(side=BOTTOM, fill=BOTH)

        def confirmbooking():
            result=admin_bookingtable()
            for row in result:
                treeview.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        confirmbooking()

        def getdatafromtreeview(a):
            bookingidfield.delete(0, END)
            pickupaddressfield.delete(0, END)
            pickuptimefield.delete(0, END)
            pickupdatefield.delete(0, END)
            dropaddressfield.delete(0, END)
            assigndriverfield.delete(0, END)

            itemselect1 = treeview.selection()[0]
            bookingidfield.insert(0,treeview.item(itemselect1)['values'][0])
            pickupaddressfield.insert(0,treeview.item(itemselect1)['values'][3])
            pickuptimefield.insert(0,treeview.item(itemselect1)['values'][6])
            pickupdatefield.insert(0,treeview.item(itemselect1)['values'][5])
            dropaddressfield.insert(0,treeview.item(itemselect1)['values'][4])

        treeview.bind('<<TreeviewSelect>>', getdatafromtreeview)




        # adding widgets on add driver frame
        namelabel = Label(adddriverframe, text='Name', font=font, bg='alice blue')
        namelabel.place(x=20, y=20)

        nametxt= Entry(adddriverframe, font=font)
        nametxt.place(x=120, y=20)

        emaillbl = Label(adddriverframe, text='Email', font=font, bg='alice blue')
        emaillbl.place(x=20, y=70)

        emailtxt = Entry(adddriverframe, font=font)
        emailtxt.place(x=120, y=70)

        licenselbl = Label(adddriverframe, text='License No', font=font, bg='alice blue')
        licenselbl.place(x=20, y=120)

        licensetxt = Entry(adddriverframe, font=font)
        licensetxt.place(x=120, y=120)

        addresslbl = Label(adddriverframe, text='Address', font=font, bg='alice blue')
        addresslbl.place(x=370, y=20)

        addresstxt = Entry(adddriverframe, font=font)
        addresstxt.place(x=470, y=20)

        passwordlbl = Label(adddriverframe, text='Password', font=font, bg='alice blue')
        passwordlbl.place(x=370, y=70)

        passwordtxt = Entry(adddriverframe, font=font)
        passwordtxt.place(x=470, y=70)

        def addDriver():
            driver1 = Driver(driver_id='', fullname=nametxt.get(), address=addresstxt.get(), email=emailtxt.get(), licenseno=licensetxt.get(), password=passwordtxt.get(), status='Active')
            result = adminadddriver(driver1)
            if result==True:
                messagebox.showinfo('Taxi Booking','Driver Added Successfully!')
                alldrivertable.delete(*alldrivertable.get_children())
                alldriver()

            else:
                messagebox.showerror('Taxi Booking', 'Error Occurred!')

        savebtn = Button(adddriverframe, text='  Save Record  ', font=font, bg='alice blue', command=addDriver)
        savebtn.place(x=780, y=20)

        def clearfunction():
            nametxt.delete(0, END)
            addresstxt.delete(0, END)
            emailtxt.delete(0, END)
            licensetxt.delete(0, END)
            passwordtxt.delete(0, END)

        clearbtn = Button(adddriverframe, text='   Clear Field   ', font=font, bg='alice blue', command=clearfunction)
        clearbtn.place(x=780, y=120)

        alldrivertable = ttk.Treeview(adddriverframe, height=18)
        alldrivertable.pack(side=BOTTOM, fill=BOTH)
        alldrivertable['columns']=('did', 'fullname','address','email','licenseno')
        alldrivertable.column('#0', width=0, stretch=0)
        alldrivertable.column('did', width=100, anchor=CENTER)
        alldrivertable.column('fullname', width=100, anchor=CENTER)
        alldrivertable.column('address', width=100, anchor=CENTER)
        alldrivertable.column('email', width=100, anchor=CENTER)
        alldrivertable.column('licenseno', width=100, anchor=CENTER)

        alldrivertable.heading('#0', text='', anchor=CENTER)
        alldrivertable.heading('did', text='Driver Id', anchor=CENTER)
        alldrivertable.heading('fullname', text='Full Name', anchor=CENTER)
        alldrivertable.heading('address', text='Address', anchor=CENTER)
        alldrivertable.heading('email', text='Email', anchor=CENTER)
        alldrivertable.heading('licenseno', text='License No', anchor=CENTER)

        def alldriver():
            tabledriver = driverontable()
            for x in tabledriver:
                alldrivertable.insert(parent='', index='end', values=(x[0], x[1], x[2], x[3], x[4]))
        alldriver()



if __name__ == '__main__':
    root=Tk()
    AdminDashboard(root)
    root.mainloop()