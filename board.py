import pygame 

import cards
import spice
import marketcard

class Board:
    market = []
    traders = []

def draw_marketplace(canvas,market):
    #canvaswidth = 1000
    #canvaslength = 800
    spacebetweencards = 20
    numberofcards = 5
    cardlocationy = 130
    cardheight = 160
    cardwidth = 120 #old: (canvaswidth - ((numberofcards+1) * spacebetweencards))/ numberofcards
    
    
    pygame.draw.rect(canvas, (200,0,0), pygame.Rect(10,10,980,300))
    font = pygame.font.Font(None, 100)
    text = font.render("Marketplace", True, (50,0,0))
    text_rect = text.get_rect(center=(500, 50))
    canvas.blit(text, text_rect)
    
    #draw marketcards
    for x in range(numberofcards):

        cardlocationx = spacebetweencards*(1+x)+x*cardwidth

        newmarketcard = marketcard.Marketcard(cardlocationx,cardlocationy)
        market.append(newmarketcard)
        newmarketcard.draw_card(canvas)

        #draw spices on cards
        blocklocation = 1
        marketcardspices = newmarketcard.spices

        for y in marketcardspices:
            printblock = True
            
            color = (0,0,0)
            if  y > 0 & y <= 4:
                newspicelocationx = cardlocationx + (20*blocklocation)
                newspicelocationy = cardlocationy+(cardheight/2)
                newspice = spice.Spice(y,newspicelocationx,newspicelocationy)
                newspice.draw_spice(canvas)
                
            elif y > 4 & y < 0: #shouldnt happen but just in case
                print('error in making spices in drawing marketcards')
            #else is when y=0, in this case no spice is drawn, which is correct

            blocklocation = blocklocation+1


