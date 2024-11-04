import cards
import pygame

class Tradercard(cards.Cards):
    type = 'tradercard'
    color = (0,0,50)

    def __init__(self,action,locationx,locationy):
        self.action = action
        self.locationx = locationx
        self.locationy = locationy

    def draw_tradercard(self,canvas):
        pygame.draw.rect(canvas, self.color, pygame.Rect(self.locationx,self.locationy,self.cardwidth,self.cardheight))
        #TODO: Add card characteristics (action, number of blocks, which colors)

def load_all_traders():
    traders = []
    startingtraders = []

    f = open("traders-exchange.txt", "r")
    for x in f:
        line = x.replace('\n','')
        traders.append([int(x) for x in str(line)])
    f.close()

    f = open("traders-gain.txt", "r")
    count=0
    for x in f:
        line = x.replace('\n','')
        traders.append([int(x) for x in str(line)])
        if count == 0:
            startingtraders.append([int(x) for x in str(line)])
        count=count+1
    f.close()

    f = open("traders-upgrade.txt", "r")
    count=0
    for x in f:
        line = x.replace('\n','')
        traders.append([int(x) for x in str(line)])
        if count == 0:
            startingtraders.append([int(x) for x in str(line)])
        count=count+1
    f.close()