from tkinter import *
from PIL import ImageTk, Image
from backend.cusDbms import saveCustomer
from frontend import Login
from middleware.customerlibrary import Customer

class registration():
    def __init__(self, reg):
        self.reg=reg
        self.reg.geometry("1000x500")
        self.reg.title("Registration")
        self.reg.config(background="alice blue")


        lblName= Label(self.reg, text="Name:",bg="alice blue", font=('Arabic', 10, 'bold'))
        lblName.place(x=40, y=50)

        lblAddress= Label(self.reg, text="Address:",bg="alice blue", font=('Arabic', 10, 'bold'))
        lblAddress.place(x=40, y=100)

        lblEmail= Label(self.reg, text="Email:",bg="alice blue", font=('Arabic', 10, 'bold'))
        lblEmail.place(x=40, y=150)

        lbPhone= Label(self.reg, text="Phone:",bg="alice blue", font=('Arabic', 10,'bold' ))
        lbPhone.place(x=40, y=200)
        lblUser= Label(self.reg, text="Username:", bg="alice blue",font=('Arabic', 10,'bold' ))
        lblUser.place(x=40, y=250)

        lblpassword= Label(self.reg, text="Password:",bg="alice blue", font=('Arabic', 10,'bold' ))
        lblpassword.place(x=40, y=300)

        txtname = Entry()
        txtname.place(x=120, y=50)

        txtaddress= Entry()
        txtaddress.place(x=120, y=100)

        txtemail= Entry()
        txtemail.place(x=120, y=150)

        txtphone= Entry()
        txtphone.place(x=120, y=200)

        txtuser= Entry()
        txtuser.place(x=130, y=250)

        txtpassword = Entry()
        txtpassword.place(x=130, y=300)

        canvas = Canvas(reg, width=700, height=400)
        canvas.place(x=300)
        self.reg.image = ImageTk.PhotoImage(Image.open("taxiiiiii.jpg"))
        canvas.create_image(10, 10, anchor=NW, image=self.reg.image)


        def cusRegistration():
            reg = Customer(cus_id='', cus_name=txtname.get(), cus_address=txtaddress.get(), cus_email=txtemail.get(), cus_phone=txtphone.get(), cus_username=txtpassword.get(),
                           cus_password=txtpassword.get())
            result= saveCustomer(reg)
            if result== True:
                print("save")
            else:
                print("error")

        btnRegister= Button(text='Register',bg="alice blue", font=('Arabic', 12,'bold' ), command=cusRegistration)
        btnRegister.place(x=60, y=370)

        def backtologin():
            self.reg.destroy()
            win = Tk()
            Login.login(win)
            win.mainloop()

        btnLog= Button(text="Back to Login",bg="alice blue", font=('Arabic', 12,'bold' ), command=backtologin)
        btnLog.place(x=150, y=370)

if __name__ == "__main__":
    reg = Tk()
    registration(reg)
    reg.mainloop()
