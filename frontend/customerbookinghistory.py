from tkinter import *
from tkinter import ttk

from backend.bookingDBMS import customerbookinghistory
from middleware import Global


class BookingHistory():
    def __init__(self, root):
        self.root=root
        self.root.title("Customer Booking History")
        frame_width = 900
        frame_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.root.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate, y_cordinate))

        custID=Entry(self.root)
        custID.insert(0, Global.currentuser[0])

        treeview=ttk.Treeview(self.root)
        treeview.pack(side=TOP, fill=BOTH, expand=TRUE)

        treeview['columns']=('id','pickup','dropodd','date','time')
        treeview.column('#0', width=0, stretch=0)
        treeview.column('id',width=100, anchor=CENTER)
        treeview.column('pickup', width=100, anchor=CENTER)
        treeview.column('dropodd', width=100, anchor=CENTER)
        treeview.column('date', width=100, anchor=CENTER)
        treeview.column('time', width=100, anchor=CENTER)

        treeview.heading('#0', text='', anchor=CENTER)
        treeview.heading('id',text="ID", anchor=CENTER)
        treeview.heading('pickup', text="Pickup", anchor=CENTER)
        treeview.heading('dropodd', text="Dropoff", anchor=CENTER)
        treeview.heading('date', text="Pickup Date", anchor=CENTER)
        treeview.heading('time', text="Pickup Time", anchor=CENTER)

        def table():
            customerdata=customerbookinghistory(custID.get())
            for a in customerdata:
                treeview.insert(parent='', index='end', values=(a[0],a[1],a[2],a[3],a[4]))

        table()

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


if __name__=='__main__':
    root=Tk()
    BookingHistory(root)
    root.mainloop()