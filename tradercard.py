import cards
import pygame
import spice
import random

class Tradercard(cards.Cards):
    type = 'tradercard'
    color = (0,0,50)

    def __init__(self,action,locationx,locationy):
        self.action = action
        self.locationx = locationx
        self.locationy = locationy

    def draw_tradercard(self,canvas,cardinfo):
        card_x = self.locationx
        card_y = self.locationy
        pygame.draw.rect(canvas, self.color, pygame.Rect(self.locationx,self.locationy,self.cardwidth,self.cardheight))

        #TODO: Add card characteristics (action, number of blocks, which colors)
        #which action is defined by len(cardinfo), length 8 is an exchange card, length 4 is a gain, length 1 is an upgrade.
        match len(cardinfo):
            case 1:
                #draw arrow with upgrade number written on it:
                pygame.draw.polygon(canvas, (0, 200, 0), ((card_x+20, card_y+40), (card_x+30, card_y+40), (card_x+30, card_y+30), (card_x+40, card_y+30), (card_x+25, card_y+0), (card_x+10, card_y+30), (card_x+20, card_y+30)))
                font = pygame.font.Font(None, 30)
                text = font.render(str(*cardinfo), True, (50,50,50)) # the * before cardinfo prints the contents of the list without brackets
                canvas.blit(text,(card_x+20,card_y+20))
                cardtype = "update"

            case 4:
                #for each type draw the spices
                spice.Spice.draw_list_of_spices(canvas, card_x+10, card_y+10, cardinfo, "y")
                        
                cardtype = "gain"
                
            case 8:
                #split in 2x4 and do the same as with displaying spices for gain, but left to right instead of down.

                #draw upside down arrow
                pygame.draw.polygon(canvas, (0, 200, 0), ( (card_x+40, card_y+30), (card_x+25, card_y+50), (card_x+10, card_y+30)))

                #draw exchangefrom spices
                exchangefrom = cardinfo[0:4]
                spice.Spice.draw_list_of_spices(canvas, card_x+10, card_y+10, exchangefrom, "x")
                
                #draw exchange into spices:
                exchangeinto = cardinfo[4:8]
                spice.Spice.draw_list_of_spices(canvas, card_x+10, card_y+50, exchangeinto, "x")

                cardtype = "exchange"
            case _:
                raise Exception("error while drawing tradercard")
            
        font = pygame.font.Font(None, 30)
        text = font.render(str(cardtype), True, (50,50,250)) 
        canvas.blit(text,(card_x+10,card_y+120))

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

    random.shuffle(traders)

    return traders

def gain(n):
    # expects numbers [#,#,#,#] as input
    print("Gain action triggered")

def upgrade(n):
    #expects an integer as input (numbers 1-4)
    print("upgrade action triggered")

def exchange(n):
    #expects numbers [#,#,#,#],[#,#,#,#] as input
    print("exchange action triggered")