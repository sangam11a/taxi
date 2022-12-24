class Driver():
    def __init__(self, driver_id=0, fullname=None, address=None, email=None, licenseno=None, status=None, password=None):
        self.driver_id=driver_id
        self.fullname=fullname
        self.address=address
        self.email=email
        self.licenseno=licenseno
        self.status=status
        self.password=password

    def getDriver_id(self):
        return self.driver_id

    def getFullname(self):
        return self.fullname

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email

    def getLicenseno(self):
        return self.licenseno

    def getStatus(self):
        return self.status

    def getPassword(self):
        return self.password

    def setDriver_id(self, driver_id):
        self.driver_id=driver_id

    def setFullname(self, fullname):
        self.fullname=fullname

    def setAddress(self, address):
        self.address=address

    def setEmail(self, email):
        self.email=email

    def setLicensenno(self, licenseno):
        self.licenseno=licenseno

    def setStatus(self, status):
        self.status=status

    def setPassword(self, password):
        self.password=password

    def __str__(self):
        return '{},{},{},{},{},{},{}'.format(self.driver_id, self.fullname, self.address, self.email, self.licenseno, self.status, self.password)