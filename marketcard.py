import cards
import random
import pygame
import spice

class Marketcard(cards.Cards):
    type = 'marketcard'
    color = (50,0,0)
    spices = []
    points = 0

    def __init__(self,locationx,locationy):
        self.locationx = locationx
        self.locationy = locationy

        #add spices to the card: have 1 random number between 1-4 and the others between 0-4 causes all cards to at least require 1 spice.
        self.spices = [random.randint(1,4),random.randint(0,4),random.randint(0,4),random.randint(0,4)]
        self.spices.sort()
        self.points = sum(self.spices)

    def draw_card(self,canvas):
        pygame.draw.rect(canvas, self.color, pygame.Rect(self.locationx,self.locationy,self.cardwidth,self.cardheight))
        
        #draw points on card:
        font = pygame.font.Font(None, 100)
        text = font.render(str(self.points), True, (100+self.points*10,50,50))
        text_rect = text.get_rect(center=(self.locationx+ (self.cardwidth/2), self.locationy+(self.locationy/3)))
        canvas.blit(text, text_rect)
        
        #draw spices on cards
        blocklocation = 1
        marketcardspices = self.spices

        for y in marketcardspices:
            if  y > 0 & y <= 4:
                newspicelocationx = self.locationx + (20*blocklocation)
                newspicelocationy = self.locationy+(self.cardheight/2)
                newspice = spice.Spice(y,newspicelocationx,newspicelocationy)
                newspice.draw_spice(canvas)
                
            elif y > 4 & y < 0: #shouldnt happen but just in case
                print('error in making spices in drawing marketcards')
            #else is when y=0, in this case no spice is drawn, which is correct

            blocklocation = blocklocation+1