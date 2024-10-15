import pygame 

import cards
import spice

class Board:
    market = cards.create_marketcards(5)
    traders = []

def draw_marketplace(canvas,market):
    canvaswidth = 1000
    canvaslength = 800
    spacebetweencards = 20
    numberofcards = 5
    startcardheight = 130
    cardheight = 160
    cardwidth = (canvaswidth - ((numberofcards+1) * spacebetweencards))/ numberofcards
    
    
    pygame.draw.rect(canvas, (200,0,0), pygame.Rect(10,10,980,300))
    font = pygame.font.Font(None, 100)
    text = font.render("Marketplace", True, (50,0,0))
    text_rect = text.get_rect(center=(500, 50))
    canvas.blit(text, text_rect)
    
    #draw marketcards
    for x in range(numberofcards):
        currentmarketcard = market[x]
        startwidthofthiscard = spacebetweencards*(1+x)+x*cardwidth
        pygame.draw.rect(canvas, (50,0,0), pygame.Rect(startwidthofthiscard,startcardheight,cardwidth,cardheight))
        print(market[x])

        #draw spices on cards
        blocklocation = 1
        for y in currentmarketcard:
            printblock = True
            
            color = (0,0,0)
            if  y == 0:
                print('found a zero')
                #donothing
            elif y > 0 & y <= 4:
                newspicelocationx = startwidthofthiscard + (20*blocklocation)
                newspicelocationy = startcardheight+(cardheight/2)
                newspice = spice.Spice(y,newspicelocationx,newspicelocationy)
                newspice.draw_spice(canvas)
                
            else: #shouldnt happen but just in case
                print('error in making spices in drawing marketcards')

            blocklocation = blocklocation+1


