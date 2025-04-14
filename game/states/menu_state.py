import pygame

class MenuState:
    
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font_title = pygame.font.Font(None, 64)
        self.font_menu = pygame.font.Font(None, 36)
        
        self.menu_options = ["Nouvelle Partie", "Instructions", "Quitter"]
        self.selected_option = 0
        
        self.title_color = (255, 255, 0)
        self.option_color = (200, 200, 200)
        self.selected_color = (255, 255, 255)
    
    def enter(self):
        pass
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.menu_options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.menu_options)
            elif event.key == pygame.K_RETURN:
                self.select_option()
    
    def select_option(self):
        if self.selected_option == 0:
            self.game_manager.change_state('play')
        elif self.selected_option == 1:
            self.game_manager.change_state('instructions')
        elif self.selected_option == 2:
            pygame.quit()
            import sys
            sys.exit()
    
    def update(self):
        pass
    
    def render(self, screen):

        title_text = self.font_title.render("ESCAPE THE MAZE", True, self.title_color)
        title_rect = title_text.get_rect(center=(screen.get_width() // 2, 100))
        screen.blit(title_text, title_rect)
        

        for i, option in enumerate(self.menu_options):
            color = self.selected_color if i == self.selected_option else self.option_color
            option_text = self.font_menu.render(option, True, color)
            option_rect = option_text.get_rect(center=(screen.get_width() // 2, 250 + i * 50))
            screen.blit(option_text, option_rect)