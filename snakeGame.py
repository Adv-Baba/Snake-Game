# import required modules
import pygame
import time
import random

# initialize pygame modules
pygame.init()

# define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set the window size and title
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# define font for displaying score
font_style = pygame.font.SysFont(None, 30)

# Draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, BLACK, [x[0], x[1], snake_block, snake_block])

# Draw the food
def draw_food(snake_block, foodx, foody):
    pygame.draw.rect(window, RED, [foodx, foody, snake_block, snake_block])

# Update the display
def update_display():
    pygame.display.update()

# Main game loop
game_over = False
clock = pygame.time.Clock()

# Set the initial position of the snake
x1 = WINDOW_WIDTH / 2
y1 = WINDOW_HEIGHT / 2
x1_change = 0
y1_change = 0

# Set the size of the snake and the food
snake_block = 10
foodx = round(random.randrange(0, WINDOW_WIDTH - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, WINDOW_HEIGHT - snake_block) / 10.0) * 10.0

# Set the initial length of the snake
snake_list = []
snake_length = 1

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Handle input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x1_change = snake_block
        y1_change = 0
    elif keys[pygame.K_LEFT]:
        x1_change = -snake_block
        y1_change = 0
    elif keys[pygame.K_UP]:
        y1_change = -snake_block
        x1_change = 0
    elif keys[pygame.K_DOWN]:
        y1_change = snake_block
        x1_change = 0

    # Update the position of the snake's head
    x1 += x1_change
    y1 += y1_change

    # Check if the snake has collided with the food
    if x1 == foodx and y1 == foody:
        print("Yummy!!")
        foodx = round(random.randrange(0, WINDOW_WIDTH - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, WINDOW_HEIGHT - snake_block) / 10.0) * 10.0
        snake_length += 1

    # Fill the screen with blue
    window.fill((0, 0, 255))

    # Draw the snake and the food
    snake_head = [x1, y1]
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    draw_snake(snake_block, snake_list)
    draw_food(snake_block, foodx, foody)

    # Update the display
    update_display()

    # Check if the snake has collided with the boundaries of the window
    if x1 >= WINDOW_WIDTH or x1 < 0 or y1 >= WINDOW_HEIGHT or y1 < 0:
        game_over = True

    clock.tick(5)

# Quit Pygame
pygame.quit()

# Quit the program
quit()
