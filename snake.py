import sys
import random
import pygame

# Initialize Pygame
pygame.init()

# Set up some constants and initialize variables
WIDTH, HEIGHT = 600, 400
SNAKE_SIZE = 20
FPS = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, (x, y, SNAKE_SIZE, SNAKE_SIZE))

def draw_food(food_pos):
    pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], SNAKE_SIZE, SNAKE_SIZE))

def game_over():
    font = pygame.font.SysFont(None, 50)
    text = font.render("GAME OVER", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(2000)

def main():
    snake_list = [(WIDTH // 2, HEIGHT // 2)]
    food_pos = (random.randint(0, WIDTH // SNAKE_SIZE) * SNAKE_SIZE, random.randint(0, HEIGHT // SNAKE_SIZE) * SNAKE_SIZE)
    x_change, y_change = SNAKE_SIZE, 0
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change != SNAKE_SIZE:
                    x_change, y_change = -SNAKE_SIZE, 0
                elif event.key == pygame.K_RIGHT and x_change != -SNAKE_SIZE:
                    x_change, y_change = SNAKE_SIZE, 0
                elif event.key == pygame.K_UP and y_change != SNAKE_SIZE:
                    x_change, y_change = 0, -SNAKE_SIZE
                elif event.key == pygame.K_DOWN and y_change != -SNAKE_SIZE:
                    x_change, y_change = 0, SNAKE_SIZE

        head_x = snake_list[-1][0] + x_change
        head_y = snake_list[-1][1] + y_change
        snake_head = (head_x, head_y)

        if not snake_list:
            snake_list.append(snake_head)
        elif snake_head == food_pos:
            score += 1
            snake_list.append(snake_head)
            food_pos = (random.randint(0, WIDTH // SNAKE_SIZE) * SNAKE_SIZE, random.randint(0, HEIGHT // SNAKE_SIZE) * SNAKE_SIZE)
        else:
            snake_list.append(snake_head)

            if len(snake_list) > score + 2:
                del snake_list[0]

        screen.fill(WHITE)
        draw_snake(snake_list)
        draw_food(food_pos)
        pygame.display.update()

        # Check for collision with boundaries and self
        if (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
            or snake_head in snake_list[:-1]
        ):
            game_over()
            break

        clock.tick(FPS)

if __name__ == "__main__":
    main()
