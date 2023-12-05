class ATXX:

    head = True
    position = 0

    def __init__(self):
        self.battery = 100

    def wait(self, distance):
        self.position += distance
        self.battery -= distance * 0.1
        return self.position
    
class ATAT(ATXX):
    def __init__(self):
        super().__init__()
        self.legs = 4
        self.armour = 50

class ATST(ATXX):
    def __init__(self):
        super().__init__()
        self.legs = 2
        self.armour = 10

class ATPT(ATXX):
    def __init__(self):
        super().__init__()
        self.legs = 2
        self.armour = 2