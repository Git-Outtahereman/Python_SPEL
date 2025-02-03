import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bombo bingbob")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Font for score and time
font = pygame.font.SysFont(None, 32)

# Score and timer


# Text positions
textX = 10
textY = 10
text2X = 10
text2Y = 30
tijdX = SCREEN_WIDTH - 120
tijdY = 10

# Function to show score


#tijdzaken
def show_tijd(x, y):
    huidig = int(pygame.time.get_ticks() / 1000)
    tijd = font.render("Time : " + str(huidig), True, PURPLE)
    screen.blit(tijd, (x, y))





# Main game loop
def GameLoop():
    winner=""
    gameOver=False
    score_value = 0
    scoreb_value = 0
    interval = 8
    laatstetijd = 0
    pwrupSize = 10
    pwrup_cooldown = 1200
    pwrup_cooldown_timer = 1200
    pwrupX = random.randint(100 , SCREEN_WIDTH-100)
    pwrupY = random.randint(50, SCREEN_HEIGHT-100)
    pwrupDur = 240
    pwrupActive = False
    
    
        
    def show_score(x, y):
        score = font.render("Score bombo : " + str(score_value), True, PURPLE)
        screen.blit(score, (x, y))

    def show_scoreb(x, y):
        scoreb = font.render("Score blauw : " + str(scoreb_value), True, PURPLE)
        screen.blit(scoreb, (x, y))

    # Player setup
    player_size = 50
    player_x = SCREEN_WIDTH // 3
    player_y = SCREEN_HEIGHT // 2
    player_speed = 10

    # Bombo setup
    bombo_size = 100
    bombo_x = SCREEN_WIDTH // 1.5
    bombo_y = SCREEN_HEIGHT // 2
    bombo_speed = 8
    huidigBombo_speed = 8
    bombo_dash = 50
    bombo_dash_duur = 5
    bombo_dash_cool = 600
    bombo_dash_cool_timer = 0
    bombo_dash_timer = 0
    bombo_is_dashing = False
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
        if keys[pygame.K_j]:
            bombo_x -= huidigBombo_speed
        if keys[pygame.K_l]:
            bombo_x += huidigBombo_speed
        if keys[pygame.K_i]:
            bombo_y -= huidigBombo_speed
        if keys[pygame.K_k]:
            bombo_y += huidigBombo_speed

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


        #dash mechanics---------------------------------------------------------------------------------------
            
         # Bombo snelheid aanpassen als hij aan het dashen is
        if bombo_is_dashing:
            huidigBombo_speed = bombo_dash
        else:
            huidigBombo_speed = bombo_speed
            
        if bombo_dash_cool_timer == 0:
            kleur1=(139,0,0)
        if bombo_dash_cool_timer > 0:
            kleur1=RED
        
        # Dash activeren (Shift indrukken)
        if keys[pygame.K_SPACE] and bombo_dash_cool_timer == 0:
            bombo_is_dashing = True
            bombo_dash_timer = bombo_dash_duur
            bombo_dash_cool_timer = bombo_dash_cool  # Zet cooldown

        # Dash-timer aftellen
        if bombo_is_dashing:
            if bombo_dash_timer > 0:
                bombo_dash_timer -= 1
        if bombo_dash_timer <= 0:
            bombo_is_dashing = False
            
        # Cooldown-timer aftellen
        if bombo_dash_cool_timer > 0:
            bombo_dash_cool_timer -= 1
        
        # Create Rect objects for collision detection
        pwrup_rect = pygame.Rect(pwrupX, pwrupY, pwrupSize, pwrupSize)
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        bombo_rect = pygame.Rect(bombo_x, bombo_y, bombo_size, bombo_size)
        
        #powerup --------------------------------------------------------------------------------------
        # Drawing everything
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player_rect)
        pygame.draw.rect(screen, kleur1, bombo_rect)
        
        if pwrup_cooldown_timer > 0:
            pwrup_cooldown_timer -= 1
        else:
            pygame.draw.rect(screen, GREEN, pwrup_rect)
        
        
        
        if pwrupActive:
            player_size = 20
        else:
            player_size = 50
        
        #powerup position
        if pwrup_cooldown_timer <= 0 and pwrup_rect.colliderect(player_rect):
            pwrupX = random.randint(100 , SCREEN_WIDTH-100)
            pwrupY = random.randint(50, SCREEN_HEIGHT-100)
            pwrup_cooldown_timer = pwrup_cooldown
            pwrupActive = True
        
        if pwrupActive:
            player_size = 20
            pwrupDur -= 1
            if pwrupDur <= 0:
                pwrupActive = False
                player_size = 50
                pwrupDur = 120
        
        

        # Collision detection
        if player_rect.colliderect(bombo_rect):
            score_value += 1  # Increase score by 1
            bombo_x = SCREEN_WIDTH // 1.5
            bombo_y = SCREEN_HEIGHT // 2
            player_x = SCREEN_WIDTH // 3
            player_y = SCREEN_HEIGHT // 2
        
            
        
        
        
        


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
    
        if score_value >= 10:
            gameOver=True
            winner="De rode speler heeft gewonnen"
        elif scoreb_value >= 10:
            gameOver=True
            winner="De blauwe speler heeft gewonnen"
        while gameOver==True:
            #winnaar tekst
            screen.fill(WHITE)
            text = font.render(winner, True, BLACK)
            text_rect = text.get_rect(center=(500, 300))
            screen.blit(text, text_rect)
            
            #restart tekst
            restart_text = font.render("Druk op R om opnieuw te starten", True, BLACK)
            restart_rect = restart_text.get_rect(center=(500, 350))
            screen.blit(restart_text, restart_rect)
            
            
            
            
            pygame.display.update()
            
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        start_tijd = pygame.time.get_ticks()
                        GameLoop()
GameLoop()        

# Quit Pygame
pygame.quit()
sys.exit()


