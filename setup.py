#something something
print ("Hello") # py .\setup.py to run it

import pygame 
import board
import player
import cards
  
pygame.init() 

#game setup  
gameBoard = board.Board()
print(gameBoard.market)

# CREATING CANVAS 
canvas = pygame.display.set_mode((1000, 800)) 
clock = pygame.time.Clock()
  
# TITLE OF CANVAS 
pygame.display.set_caption("My Board") 
running = True

board.draw_marketplace(canvas,gameBoard.market)
  

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
    clock.tick(60)  # limits FPS to 60

    pygame.display.update() 
    
