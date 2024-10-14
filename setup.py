#something something
print ("Hello") # py .\setup.py to run it

import pygame 
import board
import player
  
pygame.init() 
  
# CREATING CANVAS 
canvas = pygame.display.set_mode((1000, 1000)) 
clock = pygame.time.Clock()
  
# TITLE OF CANVAS 
pygame.display.set_caption("My Board") 
running = True
  
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
    clock.tick(60)  # limits FPS to 60

    pygame.draw.rect(canvas, (255,0,0), pygame.Rect(30,30,60,60)) 
    pygame.display.update() 
