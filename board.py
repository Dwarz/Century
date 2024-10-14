import pygame 

import cards

class Board:
    market = cards.create_marketcards(5)
    traders = []

def draw_marketplace(canvas):
    canvaswidth = 1000
    canvaslength = 800
    spacebetweencards = 20
    numberofcards = 5
    startcardheight = 130
    cardheight = 160
    cardwidth = (canvaswidth - ((numberofcards+1) * spacebetweencards))/ numberofcards
    
    
    pygame.draw.rect(canvas, (200,0,0), pygame.Rect(10,10,980,300))
    
    for x in range(numberofcards):
        pygame.draw.rect(canvas, (50,0,0), pygame.Rect(spacebetweencards*(1+x)+x*cardwidth,startcardheight,cardwidth,cardheight))
    

    font = pygame.font.Font(None, 100)
    text = font.render("Marketplace", True, (50,0,0))
    text_rect = text.get_rect(center=(500, 50))
    canvas.blit(text, text_rect)

