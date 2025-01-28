import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bombo bingbob")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Font for score and time
font = pygame.font.SysFont(None, 32)

# Score and timer
score_value = 0
scoreb_value = 0

# Text positions
textX = 10
textY = 10
text2X = 10
text2Y = 30

tijdX = 700
tijdY = 10

# Function to show score
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, PURPLE)
    screen.blit(score, (x, y))

def show_scoreb(x, y):
    scoreb = font.render("Score blauw : " + str(scoreb_value), True, PURPLE)
    screen.blit(scoreb, (x, y))

#tijdzaken
interval = 8
laatstetijd = 0


# Function to show time
def show_tijd(x, y):
    huidig = int(pygame.time.get_ticks() / 1000)
    tijd = font.render("Time : " + str(huidig), True, PURPLE)
    screen.blit(tijd, (x, y))





# Player setup
player_size = 50
player_x = SCREEN_WIDTH // 3
player_y = SCREEN_HEIGHT // 2
player_speed = 10

# Bombo setup
bombo_size = 100
bombo_x = SCREEN_WIDTH // 1.5
bombo_y = SCREEN_HEIGHT // 2
bombo_speed = 7

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling for player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed

    # Key handling for bombo
    if keys[pygame.K_LEFT]:
        bombo_x -= bombo_speed
    if keys[pygame.K_RIGHT]:
        bombo_x += bombo_speed
    if keys[pygame.K_UP]:
        bombo_y -= bombo_speed
    if keys[pygame.K_DOWN]:
        bombo_y += bombo_speed

    # Screen loop logic for player
    if player_x > SCREEN_WIDTH:
        player_x = 0 - player_size  # Reappear on the left
    elif player_x < 0 - player_size:
        player_x = SCREEN_WIDTH  # Reappear on the right
    if player_y > SCREEN_HEIGHT:
        player_y = 0 - player_size  # Reappear on the top
    elif player_y < 0 - player_size:
        player_y = SCREEN_HEIGHT  # Reappear on the bottom

    # Screen loop logic for bombo
    if bombo_x > SCREEN_WIDTH:
        bombo_x = 0 - bombo_size  # Reappear on the left
    elif bombo_x < 0 - bombo_size:
        bombo_x = SCREEN_WIDTH  # Reappear on the right
    if bombo_y > SCREEN_HEIGHT:
        bombo_y = 0 - bombo_size  # Reappear on the top
    elif bombo_y < 0 - bombo_size:
        bombo_y = SCREEN_HEIGHT  # Reappear on the bottom

    # Create Rect objects for collision detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    bombo_rect = pygame.Rect(bombo_x, bombo_y, bombo_size, bombo_size)

    # Collision detection
    if player_rect.colliderect(bombo_rect):
        score_value += 1  # Increase score by 1
        bombo_x = SCREEN_WIDTH // 1.5
        bombo_y = SCREEN_HEIGHT // 2
        player_x = SCREEN_WIDTH // 3
        player_y = SCREEN_HEIGHT // 2

    # Drawing everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, bombo_rect)


    #score blauw en tijd
    huidig = int(pygame.time.get_ticks() / 1000)
    if (huidig - laatstetijd >= interval):
        scoreb_value = scoreb_value + 1
        laatstetijd = huidig
    
    # Show score and time
    show_score(textX, textY)
    show_scoreb(text2X, text2Y)
    show_tijd(tijdX, tijdY)


    

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

