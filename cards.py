import random
import pygame

class Cards:
    locationx = 0
    locationy = 0
    cardwidth = 120
    cardheight = 160
    color = (0,0,0)

    def draw_card(self,canvas):
        pygame.draw.rect(canvas, self.color, pygame.Rect(self.locationx,self.locationy,self.cardwidth,self.cardheight))


#TODO this doesnt bleong here!
def create_marketcards(number):
        marketcards = []

        for x in range(number):
            #have 1 random number between 1-4 and the others between 0-4 causes all cards to at least require 1 spice.
            newcard = [random.randint(1,4),random.randint(0,4),random.randint(0,4),random.randint(0,4)]
            newcard.sort()
            marketcards.append(newcard)

        return marketcards
