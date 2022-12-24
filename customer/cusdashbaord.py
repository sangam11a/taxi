import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from backend.cusDashDbms import saveBooking, customertabledata, cancelrequestbycus
from frontend import Login, customerbookinghistory
from middleware import Global, booking


class CustmerDashboard123:
    def __init__(self, root):
        self.root=root
        self.root.state('zoomed')
        self.root.title("Customer Dashboard")
        self.root.config(background="alice blue")

        font=('Times New Roman',16,'normal')

        tableFrame = Frame(root, bg="ghost white", height=70)
        tableFrame.pack(side=TOP, fill=BOTH)

        home = Button(tableFrame, text="Home", bg="ghost white", bd=0, font=('Verdana', 18))
        home.place(x=130, y=25)

        # profile = Button(tableFrame, text="Profile", bg="ghost white", bd=0, font=('Verdana', 18))
        # profile.place(x=220, y=25)

        def historygui():
            root=tkinter.Toplevel()
            customerbookinghistory.BookingHistory(root)
            root.mainloop()


        history = Button(tableFrame,command=historygui, text="History", bd=0, bg="ghost white", font=('Verdana', 18),)
        history.place(x=220, y=25)

        def logoutfunction():
            self.root.destroy()
            win = Tk()
            Login.login(win)
            win.mainloop()

        Logout = Button(tableFrame,command=logoutfunction, text="Logout", bg="ghost white", bd=0, font=('Verdana', 18))
        Logout.place(x=320, y=25)

        image = Image.open('../frontend/group.png')
        image = image.resize((90, 80), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        Image_Label = Label(tableFrame, image=image)
        Image_Label.image = image
        Image_Label.place(x=10, y=0)

        side_frame = Frame(root, bg="alice blue", width=300)
        side_frame.pack(side=LEFT, fill=BOTH)


        pickupaddresslbl = Label(side_frame, text="Pickup Address", bd=0, bg="alice blue", font=font)
        pickupaddresslbl.place(x=50, y=50)

        pickupaddressfield = Entry(side_frame, font=font)
        pickupaddressfield.place(x=50, y=80)

        Pickupdatelbl = Label(side_frame, text="Pickup Date", bd=0, bg="alice blue", font=font)
        Pickupdatelbl.place(x=50, y=130)

        pickupdatefield = DateEntry(side_frame, width=15, font=font)
        pickupdatefield.place(x=50, y=160)

        pickuptimellbl = Label(side_frame, text='Pickup Time ', bd=0, bg="alice blue", font=font)
        pickuptimellbl.place(x=50, y=220)

        pickuptimefield = Entry(side_frame,font=font, width=20)
        pickuptimefield.place(x=50, y=250)

        dropofflbl = Label(side_frame, text="Drop off Address", bd=0, bg="alice blue", font=font)
        dropofflbl.place(x=50, y=290)

        dropfild = Entry(side_frame, font=font)
        dropfild.place(x=50, y=320)

        txtcid = Entry()
        txtcid.insert(0, Global.currentuser[0])
        txtcid.place()

        txtbid = Entry()

        def requestbycustomer():
            request1= booking.Booking(booking_id='',pickup_address=pickupaddressfield.get(), dropoff_address=dropfild.get(), pickup_date=pickupdatefield.get(),pickup_time=pickuptimefield.get(), status='Pending',cid=Global.currentuser[0])
            result = saveBooking(request1)
            if result == True:
                messagebox.showinfo("Taxi Booking","Booking Requested Successfully")
                table1.delete(*table1.get_children())
                getcustomerdata()

            else:
                messagebox.showerror("Taxi Booking","Error Occurred !!")

        btnrequest = Button(side_frame, text="Request Booking", bd=0, font=font, command=requestbycustomer)
        btnrequest.place(x=50, y=370)

        def cancelrequest():
            cancelcustomerdata = cancelrequestbycus(txtbid.get())
            if cancelcustomerdata == True:
                messagebox.showinfo("Taxi Booking","Booking Cancelled")
                table1.delete(*table1.get_children())
                getcustomerdata()
            else:
                messagebox.showerror("Taxi Booking", "Error Occurred !!")

        btncancel = Button(side_frame, text="Cancel Booking", bd=0, font=font, command=cancelrequest)
        btncancel.place(x=50, y=420)

        def textclear():
            txtbid.delete(0, END)
            pickupaddressfield.delete(0, END)
            dropfild.delete(0, END)
            pickupdatefield.delete(0, END)
            pickuptimefield.delete(0, END)

        btnclear = Button(side_frame, text="Clear", bd=0, font=font,command=textclear)
        btnclear.place(x=50, y=470)

        table1 = ttk.Treeview(self.root)
        table1.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
        table1['columns'] = ('Bid', 'pickup address', 'drop off address', 'pickup date', 'pickup time')
        table1.column("#0", width=0, stretch=0)
        table1.column("Bid", width=0, stretch=0)
        table1.column("pickup address", width=200, anchor=CENTER)
        table1.column('drop off address', width=200, anchor=CENTER)
        table1.column("pickup date", width=200, anchor=CENTER)
        table1.column('pickup time', width=200, anchor=CENTER)

        table1.heading("#0", text='', anchor=CENTER)
        table1.heading("Bid", text="", anchor=CENTER)
        table1.heading('pickup address', text='Pickup Address', anchor=CENTER)
        table1.heading('drop off address', text='Dropoff Address', anchor=CENTER)
        table1.heading('pickup date', text="Pickup Date", anchor=CENTER)
        table1.heading('pickup time', text="Pickup Time", anchor=CENTER)

        def getcustomerdata():
            cusdata= booking.Booking(cid=Global.currentuser[0],status='Pending')
            customerdata= customertabledata(cusdata)
            for row in customerdata:
                table1.insert(parent='',index='end',values=(row[0], row[1], row[2], row[3], row[4]))
        getcustomerdata()

        # function to get selected item values from table
        def selectcusdata(a):
            txtbid.delete(0, END)
            pickupaddressfield.delete(0, END)
            dropfild.delete(0, END)
            pickupdatefield.delete(0, END)
            pickuptimefield.delete(0, END)

            selectitem = table1.selection()[0]
            txtbid.insert(0,table1.item(selectitem)['values'][0])
            pickupaddressfield.insert(0,table1.item(selectitem)['values'][1])
            dropfild.insert(0,table1.item(selectitem)['values'][2])
            pickupdatefield.insert(0,table1.item(selectitem)['values'][3])
            pickuptimefield.insert(0,table1.item(selectitem)['values'][4])
        table1.bind('<<TreeviewSelect>>', selectcusdata)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white",
                        bordercolor="#343638",
                        borderwidth=0,
                        font=('Times New Roman', 14))
        style.map('Treeview', background=[('selected', '#22559b')])

        style.configure("Treeview.Heading",
                        background="alice blue",
                        foreground="black",
                        relief="flat",
                        font=('Times New Roman', 14))
        style.map("Treeview.Heading",
                  background=[('active', '#3484F0')], )

if __name__ == '__main__':
    root = Tk()
    CustmerDashboard123(root)
    root.mainloop()