class MenuItem:
    def __init__(self, name, price, place):
        self.name = name
        self.price = price
        self.place = place

    def show(self):
        print('{0} ({1}) @ {2}'.format(self.name, self.price, self.place))

    def is_affordable(self, yen):
        return self.price <= yen


mp = MenuItem("マンゴープリン", 280, "INIAD")
mp.show()
print(mp.is_affordable(200))
