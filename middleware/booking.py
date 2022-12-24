class Booking():
    def __init__(self, booking_id =0, pickup_address=None, dropoff_address=None, pickup_date=None, pickup_time=None, status=None, cid=None, did=None):
        self.booking_id= booking_id
        self.pickup_address=pickup_address
        self.dropoff_address=dropoff_address
        self.pickup_date=pickup_date
        self.pickup_time=pickup_time
        self.status=status
        self.cid=cid
        self.did=did

    def getBooking_id(self):
        return self.booking_id

    def getPickup_address(self):
        return self.pickup_address

    def getDropoff_address(self):
        return self.dropoff_address

    def getPickup_date(self):
        return self.pickup_date

    def getPickup_time(self):
        return self.pickup_time

    def getStatus(self):
        return self.status

    def getCid(self):
        return self.cid

    def getDid(self):
        return self.did

    def setBooking_id(self, booking_id):
        self.booking_id=booking_id

    def setPickup_address(self, pickup_address):
        self.pickup_address=pickup_address

    def setDropoff_address(self, dropoff_address):
        self.dropoff_address=dropoff_address

    def setPickup_date(self, pickup_date):
        self.pickup_date=pickup_date

    def setPickup_time(self, pickuptime):
        self.pickup_time=pickuptime

    def setStatus(self, status):
        self.status=status

    def setCid(self, cid):
        self.cid=cid

    def setDid(self, did):
        self.did=did

    def __str__(self):
        return '{},{},{},{},{},{},{},{}'.format(self.booking_id, self.pickup_address, self.dropoff_address, self.pickup_date, self.pickup_time, self.status, self.cid, self.did)