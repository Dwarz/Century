import pygame

class Spice:
    size = 19
    
    def __init__(self,type,locationx,locationy):
        self.type = type
        self.locationx = locationx
        self.locationy = locationy
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
            print("spice type = "+ str(self.type))
            raise Exception("Error in spice - updatecolor")
        
    def draw_spice(self, canvas):
        pygame.draw.rect(canvas, self.color, pygame.Rect(self.locationx,self.locationy,self.size,self.size))

    @staticmethod            
    def draw_list_of_spices(canvas, firstspice_x, firstspice_y, spicelist, direction):
        spicetype = 0
        newspicelocationx = firstspice_x
        newspicelocationy = firstspice_y
        for x in spicelist:
            spicetype += 1 #spicetypes are 1-4, so increase before using it!
            for n in range(x):
                newspice = Spice(spicetype,newspicelocationx,newspicelocationy)
                newspice.draw_spice(canvas)
                if direction == "x":
                    newspicelocationx +=20
                elif direction == "y":
                    newspicelocationy +=20
                else:
                    raise Exception("Error in drawing spice list")