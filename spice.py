class Spice:
    def __init__(self,type,locationx,locationy):
        type = 1
        locationx = 0
        locationy = 0
        size = 10
        self.updatecolor()

    def updatecolor(self):
        if self.type == 1:
            self.color = (255,223,0)
        elif self.type == 2:
            self.color = (255,0,0)
        elif self.type == 3:
            self.color = (0,255,0)
        elif self.type == 4:
            self.color = (150,75,0)
        else:
            raise Exception("Error in spice - updatecolor")
            
