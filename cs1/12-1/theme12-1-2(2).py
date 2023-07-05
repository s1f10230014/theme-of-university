class Room:
    def __init__(self, nm, ar):
        self.name = nm
        self.area = ar

    def compare(self, ar_youser):

        if self.area <= ar_youser:
            return f"{self.area} <= {ar_youser}"
        else:
            return f"{self.area} > {ar_youser}"
