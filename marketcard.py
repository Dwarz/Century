import cards
import random
import pygame

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
        #TODO: draw points on card