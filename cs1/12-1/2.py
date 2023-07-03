class MenuItem:
    def __init__(self, name, price, place):
        self.name = name
        self.price = price
        self.place = place

mp = MenuItem("マンゴープリン", 280, "INIAD")
print(mp.name, "は", mp.price, "円です")