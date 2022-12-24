class Customer():
    def __init__(self, cus_id=0, cus_name=None, cus_address=None, cus_phone=0, cus_email=None, cus_username=None, cus_password=None):
        self.cus_id=cus_id
        self.cus_name=cus_name
        self.cus_address=cus_address
        self.cus_phone=cus_phone
        self.cus_email=cus_email
        self.cus_username= cus_username
        self.cus_password= cus_password


    def getCus_id(self):
        return self.cus_id

    def getCus_name(self):
        return self.cus_name

    def  getCus_address(self):
        return self.cus_address

    def getCus_phone(self):
        return self.cus_phone

    def getCus_email(self):
        return self.cus_email

    def getCus_username(self):
        return self.cus_username

    def getCus_password(self):
        return self.cus_password

    #setter

    def setCus_id(self,cus_id):
        self.cus_id=cus_id

    def setCus_name(self, cus_name):
        self.cus_name=cus_name

    def setCus_address(self, cus_address):
        self.cus_address=cus_address

    def setCus_phone(self, cus_phone):
        self.cus_phone=cus_phone

    def setCus_email(self, cus_email):
        self.cus_email=cus_email

    def setCus_username(self, cus_username):
        self.cus_username=cus_username

    def setCus_password(self, cus_password):
        self.cus_password=cus_password

        # str/tostring
    def __str__(self):
        return ("{}, {}, {}".format(self.cus_id, self.cus_name, self.cus_address,self.cus_phone, self.cus_email,self.cus_username, self.cus_password))
