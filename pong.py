import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
WHITE = (255, 255, 255)

# Set up the paddles
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5
paddle1 = pygame.Rect(50, HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Set up the ball
BALL_WIDTH = 10
BALL_HEIGHT = 10
BALL_SPEED_X = 3
BALL_SPEED_Y = 3
ball = pygame.Rect(WIDTH/2 - BALL_WIDTH/2, HEIGHT/2 - BALL_HEIGHT/2, BALL_WIDTH, BALL_HEIGHT)
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)  # Limit the frame rate to 60 FPS

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[K_w] and paddle1.y > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[K_s] and paddle1.y < HEIGHT - PADDLE_HEIGHT:
        paddle1.y += PADDLE_SPEED
    if keys[K_UP] and paddle2.y > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[K_DOWN] and paddle2.y < HEIGHT - PADDLE_HEIGHT:
        paddle2.y += PADDLE_SPEED

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

    # Ball collision with walls
    if ball.y <= 0 or ball.y >= HEIGHT - BALL_HEIGHT:
        ball_speed_y *= -1

    # Ball reset if it leaves the screen
    if ball.x <= 0 or ball.x >= WIDTH - BALL_WIDTH:
        ball.x = WIDTH/2 - BALL_WIDTH/2
        ball.y = HEIGHT/2 - BALL_HEIGHT/2
        ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
        ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

    # Clear the screen
    win.fill(WHITE)

    # Draw the paddles and ball
    pygame.draw.rect(win, WHITE, paddle1)
    pygame.draw.rect(win, WHITE, paddle2)
    pygame.draw.ellipse(win, WHITE, ball)

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
