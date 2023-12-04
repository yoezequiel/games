import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Configuración del juego
width, height = 800, 600
cell_size = 20
speed = 10

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 128, 0)

# Crear la ventana del juego
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Inicialización del snake
snake = [(width // 2, height // 2)]
snake_direction = (cell_size, 0)

# Inicialización de la comida
food = (
    random.randint(0, (width - cell_size) // cell_size) * cell_size,
    random.randint(0, (height - cell_size) // cell_size) * cell_size,
)


# Función para dibujar el snake y la comida
def draw_elements():
    screen.fill(black)

    for row in range(0, height, cell_size):
        for col in range(0, width, cell_size):
            pygame.draw.rect(
                screen,
                green
                if (row // cell_size + col // cell_size) % 2 == 0
                else (0, 100, 0),
                (col, row, cell_size, cell_size),
            )

    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], cell_size, cell_size))

    pygame.draw.rect(screen, red, (food[0], food[1], cell_size, cell_size))


# Función para mostrar la pantalla de inicio
def show_start_screen():
    screen.fill(black)
    font = pygame.font.SysFont(None, 55)
    text = font.render("Presiona una tecla para iniciar", True, white)
    text_rect = text.get_rect(center=(width / 2, height / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False


# Función para mostrar la pantalla de Game Over
def game_over():
    screen.fill(black)
    font = pygame.font.SysFont(None, 55)
    text = font.render("Game Over", True, white)
    text_rect = text.get_rect(center=(width / 2, height / 2 - 50))
    screen.blit(text, text_rect)

    font = pygame.font.SysFont(None, 30)
    try_again_text = font.render("Presiona 'R' para intentarlo de nuevo", True, white)
    try_again_rect = try_again_text.get_rect(center=(width / 2, height / 2 + 50))
    screen.blit(try_again_text, try_again_rect)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False


# Función principal del juego
def main():
    global snake, snake_direction, food

    clock = pygame.time.Clock()

    # Mostrar la pantalla de inicio
    show_start_screen()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction[1] == 0:
                    snake_direction = (0, -cell_size)
                elif event.key == pygame.K_DOWN and snake_direction[1] == 0:
                    snake_direction = (0, cell_size)
                elif event.key == pygame.K_LEFT and snake_direction[0] == 0:
                    snake_direction = (-cell_size, 0)
                elif event.key == pygame.K_RIGHT and snake_direction[0] == 0:
                    snake_direction = (cell_size, 0)

        # Actualizar la posición del snake
        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake = [new_head] + snake[:-1]

        # Comprobar si el snake ha chocado consigo mismo o con los bordes
        if (
            new_head[0] < 0
            or new_head[0] >= width
            or new_head[1] < 0
            or new_head[1] >= height
            or new_head in snake[1:]
        ):
            game_over()
            # Reiniciar el juego si el usuario presiona 'R'
            show_start_screen()
            snake = [(width // 2, height // 2)]
            snake_direction = (cell_size, 0)
            food = (
                random.randint(0, (width - cell_size) // cell_size) * cell_size,
                random.randint(0, (height - cell_size) // cell_size) * cell_size,
            )

        # Comprobar si el snake ha comido la comida
        if new_head == food:
            snake.append(snake[-1])  # Agregar un nuevo segmento al snake
            food = (
                random.randint(0, (width - cell_size) // cell_size) * cell_size,
                random.randint(0, (height - cell_size) // cell_size) * cell_size,
            )

        # Dibujar el snake y la comida
        draw_elements()

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad del juego
        clock.tick(speed)


# Ejecutar el juego
if __name__ == "__main__":
    main()
