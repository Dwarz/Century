class Cards:
    locationx = 0
    locationy = 0
    cardwidth = 120
    cardheight = 160
    color = (0,0,0)    

    def move_to(self,newlocationx,newlocationy):
        self.locationx = newlocationx
        self.locationy = newlocationy