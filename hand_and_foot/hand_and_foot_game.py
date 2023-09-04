import pygame
import game_objects
import time
import sys

class HandAndFootGame:
    def __init__(self):
        pygame.init()
        bounds = (1024, 768)
        window = pygame.display.set_mode(bounds)
        pygame.display.set_caption("SnaPy")
        while True:
            for event in pygame.event.get():
                # process events
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                # Update your sprites

                pygame.display.update()