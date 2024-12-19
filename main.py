import pygame
import sys
from maze_generator import generate_maze

# Initialisation de Pygame
pygame.init()

# Paramètres de l'écran
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
FPS = 60

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape the Maze")

# Charger les images
player_img = pygame.image.load('assets/player.png')
wall_img = pygame.image.load('assets/wall.png')
key_img = pygame.image.load('assets/key.png')
door_img = pygame.image.load('assets/door.png')

# Génération du labyrinthe
maze_width, maze_height = WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE
maze = generate_maze(maze_width, maze_height)

# Position du joueur
player_pos = [1, 1]
has_key = False

# Fonction pour dessiner le labyrinthe
def draw_maze():
    for y, row in enumerate(maze):
        for x, tile in enumerate(row):
            if tile == 1:
                screen.blit(wall_img, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 2:
                screen.blit(key_img, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 3:
                screen.blit(door_img, (x * TILE_SIZE, y * TILE_SIZE))

# Boucle principale
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    new_pos = player_pos.copy()

    if keys[pygame.K_LEFT]:
        new_pos[0] -= 1
    if keys[pygame.K_RIGHT]:
        new_pos[0] += 1
    if keys[pygame.K_UP]:
        new_pos[1] -= 1
    if keys[pygame.K_DOWN]:
        new_pos[1] += 1

    # Gestion des collisions
    if maze[new_pos[1]][new_pos[0]] != 1:
        player_pos = new_pos

    # Collecte de la clé
    if maze[player_pos[1]][player_pos[0]] == 2:
        has_key = True
        maze[player_pos[1]][player_pos[0]] = 0

    # Ouvrir la porte si le joueur a la clé
    if maze[player_pos[1]][player_pos[0]] == 3 and has_key:
        print("Félicitations ! Vous avez réussi à sortir du labyrinthe.")
        running = False

    draw_maze()
    screen.blit(player_img, (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
