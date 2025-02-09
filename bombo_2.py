import pygame
import sys
import random
import math

# Initialiseer Pygame
pygame.init()

# Scherm grootte
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# kleuren
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GREY = (160,160,160)

# pygame scherm
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bombo bingbob")

# klok voor framerate
clock = pygame.time.Clock()

# Font voor score en tijd
font = pygame.font.SysFont(None, 32)


# Tekst positie
textX = 10
textY = 10
text2X = 10
text2Y = 30
tijdX = SCREEN_WIDTH - 120
tijdY = 10
dashX = SCREEN_WIDTH -220
dashY = 30
ScoreX = 0
ScoreY = 0
ScoreSizeX = SCREEN_WIDTH
ScoreSizeY = 70


# Gameloop voor spel
def GameLoop():
    winner=""
    gameOver=False
    score_value = 0
    scoreb_value = 0
    interval = 8
    laatstetijd = 0
    pwrupSize = 10
    pwrup_cooldown = 720 #12 seconden
    pwrup_cooldown_timer = 720
    pwrupX = random.randint(100 , SCREEN_WIDTH-100)
    pwrupY = random.randint(50, SCREEN_HEIGHT-100)
    pwrupDur = 240 #4 seconden
    bomboupDur = 420 # 7 seconden
    pwrupActive = False
    pwrupBombo = False
    Tijd = 0 # nodig voor tijd zichtbaar op scherm
    Tijdd = 0 # nodig voor correct punten geven aan blauwe speler
    Tickk = 0 # haalt ticks op
    WallSizeX = 20
    WallSizeY = 400
    WallX = pwrupX
    WallY = pwrupY - (WallSizeY / 2)
    
    
    def show_dash(x, y):
        dashtimer =  math.ceil(bombo_dash_cool_timer / 60 ) # math.ceil om naar boven af te ronden voor correcte dashcooldown.
        dash = font.render("Dashcooldown : " + str(dashtimer), True, BLACK)
        screen.blit(dash, (x, y))
        
    def show_score(x, y):
        score = font.render("Score bombo : " + str(score_value), True, BLACK)
        screen.blit(score, (x, y))

    def show_scoreb(x, y):
        scoreb = font.render("Score blauw : " + str(scoreb_value), True, BLACK)
        screen.blit(scoreb, (x, y))

    def show_tijd(x, y):
        tijd = font.render("Time : " + str(Tijd), True, BLACK)
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
    huidigBombo_speed = 7
    bombo_dash = 50
    bombo_dash_duur = 5
    bombo_dash_cool = 300
    bombo_dash_cool_timer = 0
    bombo_dash_timer = 0
    bombo_is_dashing = False # aanmaken van dash check en op false zetten zodat hij niet dasht
    running = True
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
    
    while running:
        # Event voor afsluiten
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Besturing Speler (WASD) zelf uitgevogeld met behulp van les over replit-play
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_d]:
            player_x += player_speed
        if keys[pygame.K_w]:
            player_y -= player_speed
        if keys[pygame.K_s]:
            player_y += player_speed

        # Besturing Bombo (IJKL)
        if keys[pygame.K_j]:
            bombo_x -= huidigBombo_speed
        if keys[pygame.K_l]:
            bombo_x += huidigBombo_speed
        if keys[pygame.K_i]:
            bombo_y -= huidigBombo_speed
        if keys[pygame.K_k]:
            bombo_y += huidigBombo_speed

        # Screen loop bombo
        if player_x > SCREEN_WIDTH:
            player_x = 0 - player_size  # verschijn links van het scherm
        elif player_x < 0 - player_size:
            player_x = SCREEN_WIDTH  # verschijn rechts van het schrem
        if player_y > SCREEN_HEIGHT:
            player_y = 70 - player_size  # verschijn bovenkant van het scherm
        elif player_y < 70 - player_size:
            player_y = SCREEN_HEIGHT  # verschijn onderkant van het scherm

        # Screen loop bombo
        if bombo_x > SCREEN_WIDTH:
            bombo_x = 0 - bombo_size  # Zelfde als player 
        elif bombo_x < 0 - bombo_size:
            bombo_x = SCREEN_WIDTH  # Zelfde als player 
        if bombo_y > SCREEN_HEIGHT:
            bombo_y = 70 - bombo_size  # Zelfde als player 
        elif bombo_y < 70 - bombo_size:
            bombo_y = SCREEN_HEIGHT  # Zelfde als player 


        #dash mechanics---------------------------------------------------------------------------------------
            
         # Bombo snelheid aanpassen als hij aan het dashen is
        if bombo_is_dashing:
            huidigBombo_speed = bombo_dash
        else:
            huidigBombo_speed = bombo_speed
            

        # Dash activeren (spatie indrukken)
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
        
        if bombo_dash_cool_timer == 0:
            kleur1 = (139,0,0)
        if bombo_dash_cool_timer > 0:
            kleur1 = RED
            
        # maak vierkanten voor features op scherm
        Wall_rect = pygame.Rect(WallX, WallY, WallSizeX, WallSizeY)
        text_rect = pygame.Rect(ScoreX, ScoreY, ScoreSizeX, ScoreSizeY)
        pwrup_rect = pygame.Rect(pwrupX, pwrupY, pwrupSize, pwrupSize)
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        bombo_rect = pygame.Rect(bombo_x, bombo_y, bombo_size, bombo_size)
        
        #powerup --------------------------------------------------------------------------------------
        # Draw de dingen
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
        
        #powerup positie en colision check
        if pwrup_cooldown_timer <= 0 and pwrup_rect.colliderect(player_rect):
            pwrupX = random.randint(100 , SCREEN_WIDTH-100)
            pwrupY = random.randint(50, SCREEN_HEIGHT-100)
            pwrup_cooldown_timer = pwrup_cooldown
            pwrupActive = True
        
        if pwrup_cooldown_timer <= 0 and pwrup_rect.colliderect(bombo_rect):
            pwrupBombo = True
            pwrup_cooldown_timer = pwrup_cooldown
            
        if pwrupActive:
            player_size = 20
            pwrupDur -= 1
            if pwrupDur <= 0:
                pwrupX = random.randint(100 , SCREEN_WIDTH-100)
                pwrupY = random.randint(50, SCREEN_HEIGHT-100)
                WallX = pwrupX
                WallY = pwrupY - (WallSizeY / 2)
                pwrupActive = False
                player_size = 50
                pwrupDur = 240
        #Bombo powerup muur
        if pwrupBombo:
            pygame.draw.rect(screen, BLACK, Wall_rect)
            bomboupDur -= 1
            if bomboupDur <= 0:
                pwrupBombo = False
                pwrupX = random.randint(100 , SCREEN_WIDTH-100)
                pwrupY = random.randint(50, SCREEN_HEIGHT-100)
                WallX = pwrupX
                WallY = pwrupY - (WallSizeY / 2)
                bomboupDur = 420
                
        if pwrupBombo and player_rect.colliderect(Wall_rect):
            score_value += 1  # score omhoog bij 1
            bombo_x = SCREEN_WIDTH // 1.5 # reset positie
            bombo_y = SCREEN_HEIGHT // 2 # reset positie
            player_x = SCREEN_WIDTH // 3 # reset positie
            player_y = SCREEN_HEIGHT // 2 # reset positie
            pwrupBombo = False
        

        # Collision detection
        if player_rect.colliderect(bombo_rect):
            score_value += 1  # Score omhoog met 1
            bombo_x = SCREEN_WIDTH // 1.5
            bombo_y = SCREEN_HEIGHT // 2
            player_x = SCREEN_WIDTH // 3
            player_y = SCREEN_HEIGHT // 2
        
        pygame.draw.rect(screen, GREY, text_rect)

        #score blauw en tijd
        Tickk = Tickk + 1
        Tijdd = Tickk / 60
        Tijd = int(Tijdd)
        if (Tijdd % 8 == 0):
            scoreb_value = scoreb_value + 1
        
        # score en tijd laten zien
        show_score(textX, textY)
        show_scoreb(text2X, text2Y)
        show_tijd(tijdX, tijdY)
        show_dash(dashX, dashY)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                    


        # Display updaten
        pygame.display.update()

        # frame rate
        clock.tick(60)
    
        #Restart/winscherm
        if score_value >= 10:
            gameOver=True
            winner="BOMBO heeft gewonnen"
            kleur = RED
        elif scoreb_value >= 10:
            gameOver=True
            winner="De blauwe speler heeft gewonnen"
            kleur = BLUE
        while gameOver==True:
            screen.fill(WHITE)
            text = font.render(winner, True, kleur)
            text_rect = text.get_rect(center=(500, 300))
            screen.blit(text, text_rect)
            
            #restart tekst
            restart_text = font.render("Druk op R om opnieuw te starten, of druk op Q om het spel af te sluiten", True, BLACK)
            restart_rect = restart_text.get_rect(center=(500, 350))
            screen.blit(restart_text, restart_rect)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        GameLoop()
                    if event.key == pygame.K_q:
                        sys.exit()
                    
GameLoop()        

# Quit Pygame
pygame.quit()
sys.exit()


