import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
screen_width = 600
screen_height = 150
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("T-Rex Runner")

# Load the images
dino_image = pygame.image.load("dino.png")
obstacle_image = pygame.image.load("obstacle.png")

# Set the dino's initial position and velocity
dino_x = 50
dino_y = screen_height - 50
dino_v = 0

# Set the obstacle's initial position and velocity
obstacle_x = screen_width
obstacle_y = screen_height - 50
obstacle_v = -3

# Set the game clock
clock = pygame.time.Clock()

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino_v = -5

    # Update the dino's position
    dino_y += dino_v
    dino_v += 0.5

    # Update the o