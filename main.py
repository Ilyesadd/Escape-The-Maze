#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Escape the Maze - Jeu de labyrinthe 2D
Développé avec Python et Pygame
"""

import pygame
import sys
from game.game_manager import GameManager

pygame.init()
pygame.mixer.init()  

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

def main():
  
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Escape the Maze")
    clock = pygame.time.Clock()
    
    
    game_manager = GameManager(screen)
    
    
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game_manager.handle_event(event)
        
        
        game_manager.update()
        
        
        screen.fill((0, 0, 0))  
        game_manager.render()
        pygame.display.flip()
        
        
        clock.tick(FPS)
    
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()