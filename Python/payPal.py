from payment import Payment
class PayPal(Payment):
    refer = str
    suc = str

    def __init__(self, id, refer, suc):
        super().__init__(id)
        self.refer = refer
        self.suc = suc

