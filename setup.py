#something something

import pygame 
import board
  
pygame.init() 
print("Game is running...")

#game setup  
gameBoard = board.Board()

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
    
print("Game stopped.")