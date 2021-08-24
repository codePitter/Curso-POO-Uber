from payment import Payment
from datetime import date

class creditCard(Payment):
    entity = str
    expDate = date.today()
    cvv = int

    def __init__(self, id, entity, expDate, cvv):
        super().__init__(id)
        self.entity = entity
        self.expDate = expDate
        self.cvv = cvv