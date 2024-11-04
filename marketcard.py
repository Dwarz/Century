import cards
import random
import pygame
import spice

class Marketcard(cards.Cards):
    type = 'marketcard'
    color = (50,0,0)

    def __init__(self,locationx,locationy):
        self.locationx = locationx
        self.locationy = locationy

        #add spices to the card: have 1 random number between 1-4 and the others between 0-4 causes all cards to at least require 1 spice.
        #First pick # of spices (being 4-6), then pick spice type per spice, add them to spicelist
        generatedspices = []
        numberofspices=0
        #[random.randint(1,4),random.randint(0,4),random.randint(0,4),random.randint(0,4)]
        for x in range(4):
            if numberofspices <= 2:
                number = random.randint(0,4) 
                generatedspices.append(number)
                numberofspices += number
            elif numberofspices <6:
                number = random.randint(0,6-numberofspices) 
                generatedspices.append(number)
                numberofspices += number
            else:
                generatedspices.append(0)
            #else: numberofspices is 6 or more so dont add any more spices. Note, this is a suboptimal random generator, tending to include mostly lower value blocks. good enough to program the rest of the game, but needs to be optimised later.


        self.spices = generatedspices
        self.points = generatedspices[0]*1 + generatedspices[1]*2 + generatedspices[2]*3 + generatedspices[3]*4

    def draw_marketcard(self,canvas):
        pygame.draw.rect(canvas, self.color, pygame.Rect(self.locationx,self.locationy,self.cardwidth,self.cardheight))
        
        #draw points on card:
        font = pygame.font.Font(None, 100)
        text = font.render(str(self.points), True, (90+self.points*10,50,50))
        text_rect = text.get_rect(center=(self.locationx+ (self.cardwidth/2), self.locationy+(self.locationy/3)))
        canvas.blit(text, text_rect)

        print(self.spices)
        spice.Spice.draw_list_of_spices(canvas, self.locationx+10, self.locationy+70, self.spices, "x")

        
        # #draw spices on cards
        # blocklocation = 1
        # marketcardspices = self.spices

        # for y in marketcardspices:
        #     if  y > 0 & y <= 4:
        #         newspicelocationx = self.locationx + (20*blocklocation)
        #         newspicelocationy = self.locationy+(self.cardheight/2)
        #         newspice = spice.Spice(y,newspicelocationx,newspicelocationy)
        #         newspice.draw_spice(canvas)
                
        #     elif y > 4 & y < 0: #shouldnt happen but just in case
        #         print('error in making spices in drawing marketcards')
        #     #else is when y=0, in this case no spice is drawn, which is correct

        #     blocklocation = blocklocation+1