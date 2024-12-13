import pygame
import random

# Initialize Pygame
pygame.init()

# setting constant values used to set the game
WIDTH, HEIGHT = 800, 600 
BALL_RADIUS = 10 
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_SPEED = 5

# Creating the pong game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Positioning the ball at the center of the screen and initiating movement in a random direction
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = random.choice([-1, 1]) * BALL_SPEED
ball_dy = random.choice([-1, 1]) * BALL_SPEED

# initial posittion of the 2 paddles on the left and right side of the screen
paddle1_x, paddle1_y = 50, HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_x, paddle2_y = WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2

# Initializing the score of both players to 0
score1, score2 = 0, 0
font = pygame.font.Font(None, 36)

# Loop to keep the game running
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Moving paddle based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += PADDLE_SPEED

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_RADIUS:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if (ball_x <= paddle1_x + PADDLE_WIDTH and paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT) \
            or (ball_x >= paddle2_x - BALL_RADIUS and paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT):
        ball_dx = -ball_dx
        # Increase ball speed slightly after each paddle hit
        if abs(ball_dx) < 15:  # Limit maximum speed increase
            ball_dx *= 1.1
            ball_dy *= 1.1

    # Score update
    if ball_x < 0:
        score2 += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx = random.choice([-1, 1]) * BALL_SPEED
        ball_dy = random.choice([-1, 1]) * BALL_SPEED
    elif ball_x > WIDTH:
        score1 += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx = random.choice([-1, 1]) * BALL_SPEED
        ball_dy = random.choice([-1, 1]) * BALL_SPEED

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles, ball, and score
    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)
    
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
