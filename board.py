import pygame 

import cards

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
            
            color = (0,0,0)
            if  y == 0:
                print('found a zero')
                #donothing
            elif y == 1:
                color = (255,223,0)
            elif y == 2:
                color = (255,0,0)
            elif y == 3:
                color = (0,255,0)
            elif y == 4:
                color = (150,75,0)
            else: #shouldnt happen but just in case
                print('error in making spices in drawing marketcards')

            pygame.draw.rect(canvas, color, pygame.Rect(startwidthofthiscard + (20*blocklocation),startcardheight+(cardheight/2),10,10))
            blocklocation = blocklocation+1


            


