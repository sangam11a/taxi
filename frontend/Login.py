from tkinter import *
from tkinter import messagebox
from backend.loginDbms import customerlogin, driverlogin, adminlogin
from customer import cusdashbaord
from frontend import Registration, driverdashboard, admindashboard
from middleware import Global
from middleware.customerlibrary import Customer
from middleware.driver import Driver


class login():
    def __init__(self, win):
        self.win = win
        self.win.geometry("450x450")
        self.win.resizable(False,False)
        # self.win.state("zoomed")
        self.win.config(background="alice blue")

        self.win.title("Sign In")

        #label

        lbl_heading = Label(self.win,text="Login",font=("Times New Roman",20,"bold"),bg="alice blue",fg="black",padx=20).place(x=0,y=0,relwidth=1,height=50)

        

        lbluser=Label(self.win, text="Username:",bg="alice blue", font=('Verdana', 12, 'bold'))
        lbluser.place(x=160, y=80)

        lblpass=Label(self.win, text="Password:",bg="alice blue", font=(('Verdana', 12,'bold')))
        lblpass.place(x=160, y=150)



        txtuser= Entry(width=12,text="Username", font=('Verdana', 12,'bold'))

        txtuser.place(x=160, y=110)

        txtpass= Entry(width=12, font=('Verdana', 12,'bold'), show='*')

        txtpass.place(x=160,y=180)

        def logtopage():
            txtuser1=txtuser.get()
            txtpass1=txtpass.get()
            log22=Customer(cus_username=txtuser1,cus_password=txtpass1)
            record1=customerlogin(log22)
            logdriver = Driver(email=txtuser1, password=txtpass1)
            record2 = driverlogin(logdriver)
            record3= adminlogin(logdriver)
            if record1!=None:
                messagebox.showinfo("taxi ","welcome "+record1[1])
                Global.currentuser = record1
                self.win.destroy()
                window=Tk()
                cusdashbaord.CustmerDashboard123(window)
                window.mainloop()
            elif record2 != None:
                messagebox.showinfo("taxi ", "welcome " + record2[1])
                Global.currentdriver = record2
                self.win.destroy()
                root = Tk()
                driverdashboard.DriverDashboard(root)
                root.mainloop()
            elif record3 != None:
                messagebox.showinfo("taxi ", "welcome " + record3[1])
                Global.currentdriver = record3
                self.win.destroy()
                root = Tk()
                admindashboard.AdminDashboard(root)
                root.mainloop()
            else:
                messagebox.showerror("TBS","Error")

        btnLogin=Button(text='Login', font=('Arial', 14) ,bg="alice blue", fg='black', bd=0,command=logtopage)
        btnLogin.place(x=180, y=230)

        def backtoregister():
            self.win.destroy()
            reg=Tk()
            Registration.registration(reg)
            reg.mainloop()

        btnRegister=Button(text='Dont have a account? Register here!', font=('Arial',10), bg="alice blue", fg='black', bd=0, command=backtoregister)
        btnRegister.place(x=130, y=300)

if __name__ =="__main__":
    win = Tk()
    login(win)
    win.mainloop()

