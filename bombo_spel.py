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
# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Screen Loop Example")

# Clock for controlling the frame rate
clock = pygame.time.Clock()


#score vooral van https://www.youtube.com/watch?app=desktop&v=Fp1dudhdX8k&t=0s
font = pygame.font.SysFont(None, 32)

score_value = 0
timeboard = 0

textX = 10
textY = 10

tijdX = 700
tijdY = 10
def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255, 0, 255))
    screen.blit(score, (x,y))
    
#tijd
    am_ticks = 0
def show_tijd(x,y):
    tijd = font.render("tijd : " + str(am_ticks), True, (255, 0, 255))
    screen.blit(tijd, (x,y))
# Player setup
player_size = 50
player_x = SCREEN_WIDTH // 3
player_y = SCREEN_HEIGHT // 2
player_speed = 10

bombo_size = 100
bombo_x = SCREEN_WIDTH // 1.5
bombo_y = SCREEN_HEIGHT // 2
bombo_speed = 5

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bombo_x -= bombo_speed
    if keys[pygame.K_RIGHT]:
        bombo_x += bombo_speed
    if keys[pygame.K_UP]:
        bombo_y -= bombo_speed
    if keys[pygame.K_DOWN]:
        bombo_y += bombo_speed

    # Screen loop logic
    if player_x > SCREEN_WIDTH:
        player_x = 0 - player_size  # Reappear on the left
    elif player_x < 0 - player_size:
        player_x = SCREEN_WIDTH  # Reappear on the right
    if player_y > SCREEN_HEIGHT:
        player_y = 0 - player_size  # Reappear on the top
    elif player_y < 0 - player_size:
        player_y = SCREEN_HEIGHT  # Reappear on the bottom
    
    if bombo_x > SCREEN_WIDTH:
        bombo_x = 0 - bombo_size  # Reappear on the left
    elif bombo_x < 0 - bombo_size:
        bombo_x = SCREEN_WIDTH  # Reappear on the right
    if bombo_y > SCREEN_HEIGHT:
        bombo_y = 0 - bombo_size  # Reappear on the top
    elif bombo_y < 0 - bombo_size:
        bombo_y = SCREEN_HEIGHT  # Reappear on the bottom


    # Drawing everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, RED, (bombo_x, bombo_y, bombo_size, bombo_size))
    
    #score laten zien
    show_score(textX, textY)
    
    #tijdbord
    am_ticks = int(pygame.time.get_ticks()/1000)
    show_tijd(tijdX, tijdY)
    
    # Update the display
    pygame.display.update()

   
    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()