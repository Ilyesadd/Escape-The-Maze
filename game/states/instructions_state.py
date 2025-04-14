#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
État des instructions pour Escape the Maze
"""

import pygame

class InstructionsState:
    """Classe qui gère l'affichage des instructions du jeu"""
    
    def __init__(self, game_manager):
        """Initialise l'état des instructions
        
        Args:
            game_manager: Référence au gestionnaire de jeu
        """
        self.game_manager = game_manager
        self.font_title = pygame.font.Font(None, 48)
        self.font_subtitle = pygame.font.Font(None, 36)
        self.font_text = pygame.font.Font(None, 24)
        
        # Couleurs
        self.title_color = (255, 255, 0)  # Jaune
        self.subtitle_color = (255, 165, 0)  # Orange
        self.text_color = (255, 255, 255)  # Blanc
    
    def enter(self):
        """Appelé lorsque cet état devient l'état actif"""
        pass
    
    def handle_event(self, event):
        """Gère les événements pour l'écran d'instructions
        
        Args:
            event: Événement Pygame à traiter
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                self.game_manager.change_state('menu')
    
    def update(self):
        """Met à jour l'état des instructions"""
        pass
    
    def render(self, screen):
        """Dessine l'écran d'instructions
        
        Args:
            screen: Surface Pygame sur laquelle dessiner
        """
        # Dessiner le titre
        title_text = self.font_title.render("INSTRUCTIONS", True, self.title_color)
        title_rect = title_text.get_rect(center=(screen.get_width() // 2, 60))
        screen.blit(title_text, title_rect)
        
        # Dessiner les instructions
        instructions = [
            {"title": "Objectif", "text": ["Échappez du labyrinthe en trouvant la clé puis la porte de sortie.", 
                                        "Évitez les ennemis et collectez des bonus pour augmenter votre score."]},
            {"title": "Contrôles", "text": ["Flèches directionnelles : Déplacer le personnage", 
                                          "ESC : Pause / Retour au menu"]},
            {"title": "Éléments du jeu", "text": ["Joueur (cercle cyan) : Votre personnage", 
                                               "Clé (carré jaune) : À collecter pour ouvrir la porte", 
                                               "Porte (rectangle vert) : La sortie du niveau", 
                                               "Ennemis (cercles rouges) : À éviter pour ne pas perdre", 
                                               "Bonus (étoiles violettes) : Augmentent votre score"]}
        ]
        
        y_offset = 120
        for section in instructions:
            # Titre de section
            subtitle = self.font_subtitle.render(section["title"], True, self.subtitle_color)
            subtitle_rect = subtitle.get_rect(topleft=(screen.get_width() // 4, y_offset))
            screen.blit(subtitle, subtitle_rect)
            
            y_offset += 40
            
            # Texte de la section
            for line in section["text"]:
                text = self.font_text.render(line, True, self.text_color)
                text_rect = text.get_rect(topleft=(screen.get_width() // 4 + 20, y_offset))
                screen.blit(text, text_rect)
                y_offset += 30
            
            y_offset += 20
        
        # Instructions pour revenir au menu
        back_text = self.font_text.render("Appuyez sur ÉCHAP ou ENTRÉE pour revenir au menu", True, self.text_color)
        back_rect = back_text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 50))
        screen.blit(back_text, back_rect)