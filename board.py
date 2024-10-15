import pygame 
import marketcard

class Board:
    def __init__(self):
        self.market = []
        self.traders = []

    def create_marketplace(self,canvas):
        spacebetweencards = 20
        numberofcards = 5
        cardlocationy = 100
        
        pygame.draw.rect(canvas, (200,0,0), pygame.Rect(10,10,980,260))
        font = pygame.font.Font(None, 100)
        text = font.render("Marketplace", True, (50,0,0))
        text_rect = text.get_rect(center=(500, 50))
        canvas.blit(text, text_rect)
        
        #draw marketcards. NOTE: Marketcards are randomly generated.
        for x in range(numberofcards):
            #draw the first card, save the card width, with which you can then align the next cards
            if x == 0:
                cardlocationx = spacebetweencards
                newmarketcard = marketcard.Marketcard(cardlocationx,cardlocationy)
                self.market.append(newmarketcard)
                newmarketcard.draw_card(canvas)
                cardwidth = newmarketcard.cardwidth
            else:
                cardlocationx = spacebetweencards*(1+x)+x*cardwidth
                newmarketcard = marketcard.Marketcard(cardlocationx,cardlocationy)
                self.market.append(newmarketcard)
                newmarketcard.draw_card(canvas)

    def create_traders(self, canvas):
        spacebetweencards = 20
        numberofcards = 7
        cardlocationy = 300
        
        pygame.draw.rect(canvas, (100,100,200), pygame.Rect(10,300,980,260))
        font = pygame.font.Font(None, 100)
        text = font.render("Traders", True, (50,50,100))
        text_rect = text.get_rect(center=(500, 350))
        canvas.blit(text, text_rect)

        #Draw trader cards:
