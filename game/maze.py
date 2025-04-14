import pygame
import random

class Maze:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        
        self.start_pos = (1, 1)
        self.end_pos = (width - 2, height - 2)
        
        self.wall_color = (50, 50, 150)
        self.path_color = (20, 20, 20)
        self.start_color = (0, 200, 0)
        self.end_color = (200, 0, 0)
    
    def generate(self):
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        
        self.start_pos = (1, 1)
        self.end_pos = (self.width - 2, self.height - 2)
        
        self._generate_maze_recursive(self.start_pos[0], self.start_pos[1])
        
        self.grid[self.start_pos[1]][self.start_pos[0]] = 1
        self.grid[self.end_pos[1]][self.end_pos[0]] = 1
        
        self._ensure_path_to_exit()
    
    def _generate_maze_recursive(self, x, y):
        self.grid[y][x] = 1
        
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if (0 < new_x < self.width - 1 and 0 < new_y < self.height - 1 and 
                    self.grid[new_y][new_x] == 0):
                self.grid[y + dy // 2][x + dx // 2] = 1
                
                self._generate_maze_recursive(new_x, new_y)
    
    def _ensure_path_to_exit(self):
        if self._is_path_to_exit():
            return
        
        x, y = self.start_pos
        end_x, end_y = self.end_pos
        
        while x != end_x:
            x += 1 if x < end_x else -1
            self.grid[y][x] = 1
        
        while y != end_y:
            y += 1 if y < end_y else -1
            self.grid[y][x] = 1
    
    def _is_path_to_exit(self):
        visited = [[False for _ in range(self.width)] for _ in range(self.height)]
        queue = [self.start_pos]
        visited[self.start_pos[1]][self.start_pos[0]] = True
        
        while queue:
            x, y = queue.pop(0)
            
            if (x, y) == self.end_pos:
                return True
            
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                
                if (0 <= new_x < self.width and 0 <= new_y < self.height and 
                        self.grid[new_y][new_x] == 1 and not visited[new_y][new_x]):
                    queue.append((new_x, new_y))
                    visited[new_y][new_x] = True
        
        return False
    
    def get_start_position(self):
        return self.start_pos
    
    def get_end_position(self):
        return self.end_pos
    
    def get_random_empty_cell(self):
        empty_cells = []
        
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1 and (x, y) != self.start_pos and (x, y) != self.end_pos:
                    empty_cells.append((x, y))
        
        if empty_cells:
            return random.choice(empty_cells)
        else:
            return (self.width // 2, self.height // 2)
    
    def is_wall(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return True
        
        return self.grid[y][x] == 0
    
    def render(self, screen, offset_x, offset_y, cell_size):
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(
                    offset_x + x * cell_size,
                    offset_y + y * cell_size,
                    cell_size,
                    cell_size
                )
                
                if (x, y) == self.start_pos:
                    pygame.draw.rect(screen, self.start_color, rect)
                elif (x, y) == self.end_pos:
                    pygame.draw.rect(screen, self.end_color, rect)
                elif self.grid[y][x] == 0:
                    pygame.draw.rect(screen, self.wall_color, rect)
                else:
                    pygame.draw.rect(screen, self.path_color, rect)