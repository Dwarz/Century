import pygame

class Player:

    def __init__(self, playername):
        self.name = playername
        self.caravan = [3,0,0,0] #creates caravan with start resources
        self.hand = [] #TODO
        self.playedcards = [] #TODO

    #first player starts with 3x lowest spice in caravan, 

    def drawplayer(self,canvas):
        pygame.draw.rect(canvas, (50,50,50), pygame.Rect(10,600,980,260))
        font = pygame.font.Font(None, 50)
        text = font.render(str(self.name), True, (200,200,200))
        text_rect = text.get_rect(center=(100, 6250))
        canvas.blit(text, text_rect)        
        
        self.drawcaravan()


    def drawcaravan(self):
        print("Draw player caravan")

