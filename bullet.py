import pygame
from settings import BULLET_SPEED

class Bullet:

    def __init__(self, x, y):
        self.image = pygame.Surface((5, 15))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = BULLET_SPEED

    
    def update(self):
        self.rect.y -= self.speed

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)