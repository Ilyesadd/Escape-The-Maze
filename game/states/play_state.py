import pygame
from game.maze import Maze
from game.player import Player
from game.entities.enemy import Enemy
from game.entities.item import Key, Door, Bonus

class PlayState:
    
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.Font(None, 24)
        
        self.current_level = 1
        self.score = 0
        self.time_started = 0
        
        self.maze = None
        self.player = None
        self.enemies = []
        self.items = []
        
        self.cell_size = 32
        
        self.offset_x = 0
        self.offset_y = 0
        
        self.game_paused = False
        self.level_completed = False
    
    def enter(self):
        self.init_level(self.current_level)
        self.time_started = pygame.time.get_ticks()
    
    def init_level(self, level):
        maze_width = 15 + (level - 1) * 2
        maze_height = 11 + (level - 1) * 2
        
        maze_width = min(maze_width, 31)
        maze_height = min(maze_height, 23)
        
        self.maze = Maze(maze_width, maze_height)
        self.maze.generate()
        
        screen_width = self.game_manager.screen.get_width()
        screen_height = self.game_manager.screen.get_height()
        self.offset_x = (screen_width - maze_width * self.cell_size) // 2
        self.offset_y = (screen_height - maze_height * self.cell_size) // 2
        
        start_pos = self.maze.get_start_position()
        self.player = Player(start_pos[0], start_pos[1], self.cell_size)
        
        self.enemies = []
        self.items = []
        
        num_enemies = level
        for _ in range(num_enemies):
            enemy_pos = self.maze.get_random_empty_cell()
            self.enemies.append(Enemy(enemy_pos[0], enemy_pos[1], self.cell_size))
        
        key_pos = self.maze.get_random_empty_cell()
        self.items.append(Key(key_pos[0], key_pos[1], self.cell_size))
        
        door_pos = self.maze.get_end_position()
        self.items.append(Door(door_pos[0], door_pos[1], self.cell_size))
        
        num_bonus = level * 2
        for _ in range(num_bonus):
            bonus_pos = self.maze.get_random_empty_cell()
            self.items.append(Bonus(bonus_pos[0], bonus_pos[1], self.cell_size))
        
        self.level_completed = False
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game_paused = not self.game_paused
            elif event.key == pygame.K_r:
                self.init_level(self.current_level)
            elif not self.game_paused:
                if event.key == pygame.K_UP:
                    self.player.move(0, -1, self.maze)
                elif event.key == pygame.K_DOWN:
                    self.player.move(0, 1, self.maze)
                elif event.key == pygame.K_LEFT:
                    self.player.move(-1, 0, self.maze)
                elif event.key == pygame.K_RIGHT:
                    self.player.move(1, 0, self.maze)
        elif event.type == pygame.USEREVENT:
            if self.level_completed:
                pygame.time.set_timer(pygame.USEREVENT, 0)
                self.init_level(self.current_level)
    
    def update(self):
        if self.game_paused or self.level_completed:
            return
        
        self.player.update()
        
        for enemy in self.enemies:
            enemy.update(self.maze)
            
            if enemy.collides_with(self.player):
                self.game_over()
                return
        
        for item in list(self.items):
            if item.collides_with(self.player):
                if isinstance(item, Key):
                    self.player.has_key = True
                    self.items.remove(item)
                elif isinstance(item, Door):
                    if self.player.has_key:
                        self.complete_level()
                        return
                elif isinstance(item, Bonus):
                    self.score += 100
                    self.items.remove(item)
        
        current_time = pygame.time.get_ticks()
        elapsed_seconds = (current_time - self.time_started) // 1000
        time_score = max(1000 - elapsed_seconds * 10, 0)
    
    def complete_level(self):
        self.level_completed = True
        self.current_level += 1
        
        self.score += 500 * self.current_level
        
        pygame.time.set_timer(pygame.USEREVENT, 2000)
        
        if self.current_level > 10:
            self.game_manager.change_state('game_over')
            self.game_manager.states['game_over'].set_score(self.score)
    
    def game_over(self):
        
        self.game_manager.change_state('game_over')
        self.game_manager.states['game_over'].set_score(self.score)
    
    def render(self, screen):
        """Dessine le jeu sur l'écran
        
        Args:
            screen: Surface Pygame sur laquelle dessiner
        """
        self.maze.render(screen, self.offset_x, self.offset_y, self.cell_size)
        
        for item in self.items:
            item.render(screen, self.offset_x, self.offset_y)
        
        for enemy in self.enemies:
            enemy.render(screen, self.offset_x, self.offset_y)
        
        self.player.render(screen, self.offset_x, self.offset_y)
        
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        level_text = self.font.render(f"Niveau: {self.current_level}", True, (255, 255, 255))
        key_text = self.font.render(f"Clé: {'Oui' if self.player.has_key else 'Non'}", True, (255, 255, 255))
        
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))
        screen.blit(key_text, (10, 70))
        
        if self.level_completed:
            font = pygame.font.Font(None, 48)
            if self.current_level <= 10:  # Nombre total de niveaux
                message = f"Niveau {self.current_level-1} terminé!"
            else:
                message = "Félicitations! Vous avez terminé le jeu!"
            
            text = font.render(message, True, (255, 255, 0))
            text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(text, text_rect)
        
        if self.game_paused:
            font = pygame.font.Font(None, 48)
            text = font.render("PAUSE", True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(text, text_rect)