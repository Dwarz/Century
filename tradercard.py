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
                print("This is an update card")

                #draw arrow with upgrade number written on it:
                pygame.draw.polygon(canvas, (0, 200, 0), ((card_x+20, card_y+40), (card_x+30, card_y+40), (card_x+30, card_y+30), (card_x+40, card_y+30), (card_x+25, card_y+0), (card_x+10, card_y+30), (card_x+20, card_y+30)))
                font = pygame.font.Font(None, 30)
                text = font.render(str(*cardinfo), True, (50,50,50)) # the * before cardinfo prints the contents of the list without brackets
                canvas.blit(text,(card_x+20,card_y+20))
                cardtype = "update"

            case 4:
                #for each color, draw the number of spices
                print("This is a gain card")
                spicesdrawn = 0
                spicetype = 0
                newspicelocationx = card_x + 10
                newspicelocationy = card_y + 10
                for x in cardinfo:
                    spicetype += 1 #spicetypes are 1-4, so increase before using it!
                    for n in range(x):
                        newspice = spice.Spice(spicetype,newspicelocationx,newspicelocationy)
                        newspice.draw_spice(canvas)
                        spicesdrawn +=1
                        newspicelocationy +=20
                cardtype = "gain"
                
            case 8:
                print("This is an exchange card")

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