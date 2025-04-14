import pygame

class Player:
    
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        
        self.display_size = int(size * 0.8)
        
        self.color = (0, 255, 255)
        
        self.has_key = False
        
        self.animation_frame = 0
        self.animation_speed = 0.1
        
        self.target_x = x
        self.target_y = y
        self.move_speed = 0.2
    
    def move(self, dx, dy, maze):
        new_x = self.target_x + dx
        new_y = self.target_y + dy
        
        if not maze.is_wall(new_x, new_y):
            self.target_x = new_x
            self.target_y = new_y
            return True
        
        return False
    
    def update(self):
        if self.x != self.target_x or self.y != self.target_y:
            self.x += (self.target_x - self.x) * self.move_speed
            self.y += (self.target_y - self.y) * self.move_speed
            
            if abs(self.x - self.target_x) < 0.1 and abs(self.y - self.target_y) < 0.1:
                self.x = self.target_x
                self.y = self.target_y
        
        self.animation_frame += self.animation_speed
        if self.animation_frame >= 4:
            self.animation_frame = 0
    
    def render(self, screen, offset_x, offset_y):
        screen_x = offset_x + self.x * self.size + (self.size - self.display_size) // 2
        screen_y = offset_y + self.y * self.size + (self.size - self.display_size) // 2
        
        pygame.draw.circle(
            screen,
            self.color,
            (int(screen_x + self.display_size // 2), int(screen_y + self.display_size // 2)),
            self.display_size // 2
        )
        
        if self.has_key:
            key_size = self.display_size // 3
            pygame.draw.rect(
                screen,
                (255, 255, 0),
                (int(screen_x + self.display_size - key_size), 
                 int(screen_y), 
                 key_size, 
                 key_size)
            )
    
    def collides_with(self, entity):
        return round(self.x) == round(entity.x) and round(self.y) == round(entity.y)