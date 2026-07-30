price = []
class Prices:
    def __init__(self,name,bus_fee,stationaries,junk_food,mess_fee):
        self.Name = name
        self.Bus = bus_fee
        self.Stationary = stationaries
        self.junk = junk_food
        self.Mess = mess_fee
    def spent(self):
        
        global price
        price.append(self)