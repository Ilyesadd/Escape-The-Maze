#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
État de fin de jeu pour Escape the Maze
"""

import pygame

class GameOverState:
    """Classe qui gère l'état de fin de jeu"""
    
    def __init__(self, game_manager):
        """Initialise l'état de fin de jeu
        
        Args:
            game_manager: Référence au gestionnaire de jeu
        """
        self.game_manager = game_manager
        self.font_title = pygame.font.Font(None, 64)
        self.font_text = pygame.font.Font(None, 36)
        
        # Couleurs
        self.title_color = (255, 0, 0)  # Rouge
        self.text_color = (255, 255, 255)  # Blanc
        
        # Score final
        self.final_score = 0
    
    def enter(self):
        """Appelé lorsque cet état devient l'état actif"""
        # Jouer un son de game over si nécessaire
        pass
    
    def set_score(self, score):
        """Définit le score final à afficher
        
        Args:
            score: Score final du joueur
        """
        self.final_score = score
    
    def handle_event(self, event):
        """Gère les événements pour l'écran de fin de jeu
        
        Args:
            event: Événement Pygame à traiter
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                self.game_manager.change_state('menu')
    
    def update(self):
        """Met à jour l'état de fin de jeu"""
        # Animation de l'écran de fin si nécessaire
        pass
    
    def render(self, screen):
        """Dessine l'écran de fin de jeu
        
        Args:
            screen: Surface Pygame sur laquelle dessiner
        """
        # Dessiner le titre
        title_text = self.font_title.render("GAME OVER", True, self.title_color)
        title_rect = title_text.get_rect(center=(screen.get_width() // 2, 150))
        screen.blit(title_text, title_rect)
        
        # Dessiner le score
        score_text = self.font_text.render(f"Score final: {self.final_score}", True, self.text_color)
        score_rect = score_text.get_rect(center=(screen.get_width() // 2, 250))
        screen.blit(score_text, score_rect)
        
        # Instructions pour revenir au menu
        instruction_text = self.font_text.render("Appuyez sur ENTRÉE pour revenir au menu", True, self.text_color)
        instruction_rect = instruction_text.get_rect(center=(screen.get_width() // 2, 350))
        screen.blit(instruction_text, instruction_rect)