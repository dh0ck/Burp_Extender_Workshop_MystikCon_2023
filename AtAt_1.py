class ATAT:

    head = True
    position = 0

    def __init__(self):
        self.legs = 4
        self.armour = True
        self.battery = 100

    def walk(self, distance):
        self.position += distance
        self.battery -= distance * 0.1
        return self.position
    
    def fire(self, seconds):
        self.batter -= seconds * 0.01
        return self.battery