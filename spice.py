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
            raise Exception("Error in spice - updatecolor")
        
    def draw_spice(self, canvas):
        pygame.draw.rect(canvas, self.color, pygame.Rect(self.locationx,self.locationy,self.size,self.size))
            
