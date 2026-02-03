import pygame
import random
import os

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK, WHITE
from player import Player
from bullet import Bullet
from alien import Alien
from alien_bullet import AlienBullet

# INIT   

pygame.init()
pygame.mixer.init()

BASE_DIR = os.path.dirname(__file__)

shoot_sound = pygame.mixer.Sound(
    os.path.join(BASE_DIR, "sound", "shoot.wav")
)
explosion_sound = pygame.mixer.Sound(
    os.path.join(BASE_DIR, "sound", "explosion.wav")
)
game_over_sound = pygame.mixer.Sound(
    os.path.join(BASE_DIR, "sound", "game_over.wav")
)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 64)

#  OBJECTS   

player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

bullets = []
alien_bullets = []
aliens = []

# First alien wave
for x in range(100, SCREEN_WIDTH - 100, 120):
    aliens.append(Alien(x, 50))

# GAME STATE   

score = 0
game_over = False
game_over_played = False
running = True

# GAME LOOP   

while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    keys = pygame.key.get_pressed()

    # UPDATE    
    if not game_over:
        player.update(keys)

        for alien in aliens:
            alien.update()

        # Random alien shooting
        if aliens and random.randint(0, 60) == 1:
            shooter = random.choice(aliens)
            alien_bullets.append(
                AlienBullet(shooter.rect.centerx, shooter.rect.bottom)
            )

    # EVENTS    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player shooting
        if not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(
                    Bullet(player.rect.centerx, player.rect.top)
                )
                shoot_sound.play()

        # Restart game
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                score = 0
                bullets.clear()
                alien_bullets.clear()
                aliens.clear()

                for x in range(100, SCREEN_WIDTH - 100, 120):
                    aliens.append(Alien(x, 50))

                player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
                game_over = False
                game_over_played = False

    # PLAYER BULLETS    
    for bullet in bullets[:]:
        bullet.update()

        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
            continue

        for alien in aliens[:]:
            if bullet.rect.colliderect(alien.rect):
                bullets.remove(bullet)
                aliens.remove(alien)
                explosion_sound.play()
                score += 1
                break

    # ALIEN BULLETS    
    for ab in alien_bullets[:]:
        ab.update()

        if ab.rect.top > SCREEN_HEIGHT:
            alien_bullets.remove(ab)
            continue

        if ab.rect.colliderect(player.rect):
            game_over = True
            if not game_over_played:
                game_over_sound.play()
                game_over_played = True

    # RESPAWN WAVE    
    if not aliens and not game_over:
        for x in range(100, SCREEN_WIDTH - 100, 120):
            aliens.append(Alien(x, 50))

    # GAME OVER CHECK    
    for alien in aliens:
        if alien.rect.bottom >= player.rect.top:
            game_over = True
            if not game_over_played:
                game_over_sound.play()
                game_over_played = True

    # DRAW    
    player.draw(screen)

    for alien in aliens:
        alien.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    for ab in alien_bullets:
        ab.draw(screen)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    if game_over:
        over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        restart_text = font.render("Press R to Restart", True, WHITE)

        screen.blit(
            over_text,
            (SCREEN_WIDTH // 2 - 160, SCREEN_HEIGHT // 2 - 40)
        )
        screen.blit(
            restart_text,
            (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 + 10)
        )

    pygame.display.flip()

pygame.quit()
