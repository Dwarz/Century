import pygame 
import marketcard

class Board:
    market = []
    traders = []

def draw_marketplace(canvas,market):
    spacebetweencards = 20
    numberofcards = 5
    cardlocationy = 130
    cardheight = 160
    cardwidth = 120
    
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

