import pygame

class AlienBullet:
    
    def __init__(self, x, y):
        self.image = pygame.Surface((5, 15))
        self.image.fill((255, 0, 255))  #purple bullet
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 4

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)