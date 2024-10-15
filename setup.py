import pygame 
import board
import tradercard
  
pygame.init() 
print("Game is running...")

# CREATING CANVAS 
canvaswidth = 1000
canvasheight = 800
canvas = pygame.display.set_mode((canvaswidth, canvasheight)) 
clock = pygame.time.Clock()
  
# TITLE OF CANVAS 
pygame.display.set_caption("My Board") 
running = True

#game setup  
gameBoard = board.Board()

gameBoard.create_marketplace(canvas)
gameBoard.create_traders(canvas)

tradercard.load_all_traders()


  

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    clock.tick(60)  # limits FPS to 60
    pygame.display.update() 
    
print("Game stopped.")