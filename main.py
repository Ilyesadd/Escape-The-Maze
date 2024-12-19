import pygame
import sys
import random
import time
from maze_generator import generate_maze

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()

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
enemy_img = pygame.image.load('assets/enemy.png')

# Charger les fichiers audio
key_sound = pygame.mixer.Sound('assets/key.wav')
door_sound = pygame.mixer.Sound('assets/door.wav')
game_over_sound = pygame.mixer.Sound('assets/game_over.wav')

# Génération du labyrinthe
maze_width, maze_height = WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE
maze = generate_maze(maze_width, maze_height)

# Position du joueur
player_pos = [1, 1]
has_key = False

# Liste des positions des ennemis
enemies = [[5, 3], [3, 5]]

# Initialiser le temps de début pour le score
start_time = time.time()

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

# Fonction pour déplacer les ennemis aléatoirement
def move_enemies():
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for enemy in enemies:
        dx, dy = random.choice(directions)
        new_x, new_y = enemy[0] + dx, enemy[1] + dy
        if maze[new_y][new_x] == 0:
            enemy[0], enemy[1] = new_x, new_y

# Vérifier si le joueur entre en collision avec un ennemi
def check_enemy_collision():
    for enemy in enemies:
        if player_pos == enemy:
            return True
    return False

# Afficher un message à l'écran
def display_message(message, color):
    font = pygame.font.Font(None, 74)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

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

    # Gestion des collisions avec les murs
    if maze[new_pos[1]][new_pos[0]] != 1:
        player_pos = new_pos

    # Collecte de la clé
    if maze[player_pos[1]][player_pos[0]] == 2:
        has_key = True
        maze[player_pos[1]][player_pos[0]] = 0
        key_sound.play()

    # Ouvrir la porte si le joueur a la clé
    if maze[player_pos[1]][player_pos[0]] == 3 and has_key:
        door_sound.play()
        display_message("Vous avez gagné !", (0, 255, 0))
        running = False

    # Déplacer les ennemis et vérifier les collisions
    move_enemies()
    if check_enemy_collision():
        game_over_sound.play()
        display_message("Game Over !", (255, 0, 0))
        running = False

    # Dessiner le labyrinthe, le joueur et les ennemis
    draw_maze()
    screen.blit(player_img, (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE))
    for enemy in enemies:
        screen.blit(enemy_img, (enemy[0] * TILE_SIZE, enemy[1] * TILE_SIZE))

    # Mettre à jour l'affichage
    pygame.display.flip()
    clock.tick(FPS)

# Afficher le score final
end_time = time.time()
time_taken = int(end_time - start_time)
score = max(1000 - time_taken * 10, 0) + (100 if has_key else 0)
print(f"Score final : {score}")

pygame.quit()
sys.exit()
