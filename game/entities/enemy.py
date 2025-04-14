
import pygame
import random

class Enemy:
    
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        
        self.display_size = int(size * 0.7)
        
        self.color = (255, 0, 0)
        
        self.animation_frame = 0
        self.animation_speed = 0.05
        
        self.move_cooldown = 0
        self.move_delay = 30
        
        self.target_x = x
        self.target_y = y
        self.move_speed = 0.1
    
    def update(self, maze):
        if self.x != self.target_x or self.y != self.target_y:
            self.x += (self.target_x - self.x) * self.move_speed
            self.y += (self.target_y - self.y) * self.move_speed
            
            if abs(self.x - self.target_x) < 0.1 and abs(self.y - self.target_y) < 0.1:
                self.x = self.target_x
                self.y = self.target_y
        
        if self.move_cooldown <= 0 and self.x == self.target_x and self.y == self.target_y:
            self.move_randomly(maze)
            self.move_cooldown = self.move_delay
        else:
            self.move_cooldown -= 1
        
        self.animation_frame += self.animation_speed
        if self.animation_frame >= 4:
            self.animation_frame = 0
    
    def move_randomly(self, maze):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            new_x = self.target_x + dx
            new_y = self.target_y + dy
            
            if not maze.is_wall(new_x, new_y):
                self.target_x = new_x
                self.target_y = new_y
                break
    
    def render(self, screen, offset_x, offset_y):
        screen_x = offset_x + self.x * self.size + (self.size - self.display_size) // 2
        screen_y = offset_y + self.y * self.size + (self.size - self.display_size) // 2
        
        pygame.draw.rect(
            screen,
            self.color,
            (int(screen_x), int(screen_y), self.display_size, self.display_size)
        )
        
        eye_size = self.display_size // 5
        eye_offset = self.display_size // 4
        
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(screen_x + eye_offset), int(screen_y + eye_offset)),
            eye_size
        )
        
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(screen_x + self.display_size - eye_offset), int(screen_y + eye_offset)),
            eye_size
        )
    
    def collides_with(self, entity):
        return round(self.x) == round(entity.x) and round(self.y) == round(entity.y)