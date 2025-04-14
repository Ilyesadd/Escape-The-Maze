import pygame

class Item:
    
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        
        self.display_size = int(size * 0.6)
        
        self.color = (200, 200, 200)
        
        self.animation_frame = 0
        self.animation_speed = 0.05
    
    def update(self):
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
    
    def collides_with(self, entity):
        return round(self.x) == round(entity.x) and round(self.y) == round(entity.y)


class Key(Item):
    
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.color = (255, 255, 0)
    
    def render(self, screen, offset_x, offset_y):
        screen_x = offset_x + self.x * self.size + (self.size - self.display_size) // 2
        screen_y = offset_y + self.y * self.size + (self.size - self.display_size) // 2
        
        pygame.draw.rect(
            screen,
            self.color,
            (int(screen_x + self.display_size // 4), 
             int(screen_y + self.display_size // 4),
             self.display_size // 2,
             self.display_size // 2)
        )
        
        pygame.draw.rect(
            screen,
            self.color,
            (int(screen_x + self.display_size // 2 - self.display_size // 8),
             int(screen_y),
             self.display_size // 4,
             self.display_size // 2)
        )


class Door(Item):
    
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.color = (150, 75, 0)
    
    def render(self, screen, offset_x, offset_y):
        screen_x = offset_x + self.x * self.size + (self.size - self.display_size) // 2
        screen_y = offset_y + self.y * self.size + (self.size - self.display_size) // 2
        
        pygame.draw.rect(
            screen,
            self.color,
            (int(screen_x), int(screen_y), self.display_size, self.display_size)
        )
        
        pygame.draw.circle(
            screen,
            (255, 255, 0),
            (int(screen_x + self.display_size * 0.75), int(screen_y + self.display_size // 2)),
            self.display_size // 8
        )


class Bonus(Item):
    
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.color = (0, 255, 0)
        
        self.pulse_direction = 1
        self.pulse_min = 0.7
        self.pulse_max = 1.0
        self.pulse_value = 1.0
        self.pulse_speed = 0.02
    
    def update(self):
        super().update()
        
        self.pulse_value += self.pulse_direction * self.pulse_speed
        
        if self.pulse_value >= self.pulse_max:
            self.pulse_value = self.pulse_max
            self.pulse_direction = -1
        elif self.pulse_value <= self.pulse_min:
            self.pulse_value = self.pulse_min
            self.pulse_direction = 1
    
    def render(self, screen, offset_x, offset_y):
        screen_x = offset_x + self.x * self.size + (self.size - self.display_size) // 2
        screen_y = offset_y + self.y * self.size + (self.size - self.display_size) // 2
        
        pulse_size = int(self.display_size * self.pulse_value)
        
        pygame.draw.circle(
            screen,
            self.color,
            (int(screen_x + self.display_size // 2), int(screen_y + self.display_size // 2)),
            pulse_size // 2
        )