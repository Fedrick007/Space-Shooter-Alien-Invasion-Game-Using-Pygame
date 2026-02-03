import pygame
from settings import ALIEN_SPEED

class Alien:

    def __init__(self, x, y):
        self.image = pygame.Surface((40, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = ALIEN_SPEED

    def update(self):
        self.rect.y += self.speed
    

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        