import pygame 

import cards

class Board:
    market = cards.create_marketcards(5)
    traders = []

def draw_marketplace(canvas):
    startcardheight = 130
    cardheight = 160
    cardwidth = 80
    pygame.draw.rect(canvas, (200,0,0), pygame.Rect(100,10,800,400))
    pygame.draw.rect(canvas, (255,0,0), pygame.Rect(200,startcardheight,cardwidth,cardheight))
    pygame.draw.rect(canvas, (255,0,0), pygame.Rect(300,startcardheight,cardwidth,cardheight))
    pygame.draw.rect(canvas, (255,0,0), pygame.Rect(400,startcardheight,cardwidth,cardheight))
    pygame.draw.rect(canvas, (255,0,0), pygame.Rect(500,startcardheight,cardwidth,cardheight)) 
    pygame.draw.rect(canvas, (255,0,0), pygame.Rect(600,startcardheight,cardwidth,cardheight))
    pygame.draw.rect(canvas, (255,0,0), pygame.Rect(600,startcardheight,cardwidth,cardheight))
