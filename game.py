import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Configurações da tela
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Inicialização da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Inicialização da fonte
font = pygame.font.Font(None, 36)

# Função para desenhar a cobra
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Função para desenhar a comida
def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Função para mostrar a mensagem de Game Over
def game_over_message():
    game_over_text = font.render("GAME OVER", True, RED)
    screen.blit(game_over_text, [WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2])
    pygame.display.flip()
    pygame.time.wait(2000)

# Função principal do jogo
def main():
    running = True
    while running:
        snake = [[5, 5]]
        food = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]
        dx, dy = 1, 0
        clock = pygame.time.Clock()
        game_over = False

        while not game_over:
            screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and dy != 1:
                        dx, dy = 0, -1
                    elif event.key == pygame.K_DOWN and dy != -1:
                        dx, dy = 0, 1
                    elif event.key == pygame.K_LEFT and dx != 1:
                        dx, dy = -1, 0
                    elif event.key == pygame.K_RIGHT and dx != -1:
                        dx, dy = 1, 0

            new_head = [snake[0][0] + dx, snake[0][1] + dy]
            snake.insert(0, new_head)

            if snake[0] == food:
                food = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]
            else:
                snake.pop()

            draw_snake(snake)
            draw_food(food)

            # Verificação de colisão com as paredes
            if (snake[0][0] < 0 or snake[0][0] >= GRID_WIDTH or
                snake[0][1] < 0 or snake[0][1] >= GRID_HEIGHT):
                game_over = True

            # Verificação de colisão com o próprio corpo
            if len(snake) != len(set(map(tuple, snake))):
                game_over = True

            pygame.display.flip()
            clock.tick(10)

        game_over_message()

    pygame.quit()

if __name__ == "__main__":
    main()
