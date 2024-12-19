import random

def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    stack = []
    start_x, start_y = 1, 1
    maze[start_y][start_x] = 0
    stack.append((start_x, start_y))

    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]

    while stack:
        x, y = stack[-1]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width-1 and 1 <= ny < height-1 and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[y + dy//2][x + dx//2] = 0
                stack.append((nx, ny))
                break
        else:
            stack.pop()

    # Ajouter une clé et une porte
    maze[1][width-2] = 2  # Clé
    maze[height-2][width-2] = 3  # Porte

    return maze
