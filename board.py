import pygame 
import marketcard
import tradercard

class Board:
    def __init__(self):
        self.market = []
        self.traders = []

    def create_marketplace(self,canvas):
        spacebetweenmarketcards = 20
        numberofmarketcards = 5
        marketcardlocationy = 100
        
        pygame.draw.rect(canvas, (200,0,0), pygame.Rect(10,10,980,260))
        font = pygame.font.Font(None, 100)
        text = font.render("Marketplace", True, (50,0,0))
        text_rect = text.get_rect(center=(500, 50))
        canvas.blit(text, text_rect)
        
        #draw marketcards. NOTE: Marketcards are randomly generated.
        for x in range(numberofmarketcards):
            #draw the first card, save the card width, with which you can then align the next cards
            if x == 0:
                cardlocationx = spacebetweenmarketcards
                newmarketcard = marketcard.Marketcard(cardlocationx,marketcardlocationy)
                self.market.append(newmarketcard)
                newmarketcard.draw_marketcard(canvas)
                marketcardwidth = newmarketcard.cardwidth
            else:
                cardlocationx = spacebetweenmarketcards*(1+x)+x*marketcardwidth
                newmarketcard = marketcard.Marketcard(cardlocationx,marketcardlocationy)
                self.market.append(newmarketcard)
                newmarketcard.draw_marketcard(canvas)

    def create_traders(self, canvas):
        spacebetweentradercards = 20
        numberoftradercards = 7
        tradercardlocationy = 390
        
        pygame.draw.rect(canvas, (100,100,200), pygame.Rect(10,300,980,260))
        font = pygame.font.Font(None, 100)
        text = font.render("Traders", True, (50,50,100))
        text_rect = text.get_rect(center=(500, 350))
        canvas.blit(text, text_rect)

        for x in range(numberoftradercards):
            if x == 0:
                cardlocationx = spacebetweentradercards
                newtradercard = tradercard.Tradercard("test",cardlocationx,tradercardlocationy)
                self.traders.append(newtradercard)
                newtradercard.draw_tradercard(canvas)
                tradercardwidth = newtradercard.cardwidth
            else:
                cardlocationx = spacebetweentradercards*(1+x)+x*tradercardwidth
                newtradercard = tradercard.Tradercard("test",cardlocationx,tradercardlocationy)
                self.traders.append(newtradercard)
                newtradercard.draw_tradercard(canvas)



