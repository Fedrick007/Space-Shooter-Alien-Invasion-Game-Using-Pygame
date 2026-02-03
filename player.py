import pygame
from settings import PLAYER_SPEED, SCREEN_WIDTH

class Player(pygame.sprite.Sprite):

    def __init__(self, x,y):
        self.image = pygame.Surface((50, 40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = PLAYER_SPEED


    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)





