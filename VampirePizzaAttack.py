#import libraries
import pygame
from pygame import *
# initialize pygame
pygame.init()

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

# create window
GAME_WINDOW = display.set_mode(WINDOW_RES)
# add window caption
display.set_caption('Attack of the Vampire Pizzas!')

# set up enemy image
# load image into program
pizza_img = image.load('vampire.png')
# convert img to a surface
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (100, 100))
GAME_WINDOW.blit(VAMPIRE_PIZZA, (900, 400))

# main event loop
game_running = True
while game_running:
    # check for events
    for event in pygame.event.get():
        # exit loop on quit
        if event.type == QUIT:
            game_running = False
        display.update()

# end of main game loop, clean up game
pygame.quit()
