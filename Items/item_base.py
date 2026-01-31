import pygame
import sys
import random
from pathlib import Path


class item:
    pos = pygame.Vector2()
    script_dir = Path(__file__).parent
    apple = pygame.image.load(script_dir / "../Icons/apple.png")
    applerect = apple.get_rect()


    def __init__(self, screen):
        self.pos = pygame.Vector2(random.randint(0,screen.width - 50), random.randint(0,screen.height - 50))

    def add_item(self, screen):
        self.apple = pygame.transform.scale(self.apple, (30,30))
        self.applerect.size = (30,30)
        self.applerect.center = self.pos
        screen.blit(self.apple, self.applerect)
        return screen
    
    def check_colide(self, player_rec, enemy_rec, screen):
        if self.applerect.colliderect(player_rec) or self.applerect.colliderect(enemy_rec):
            self.pos = pygame.Vector2(random.randint(0,screen.width - 50), random.randint(0,screen.height - 50))
            return screen
        
    def get_apple_pos(self):
        return self.pos
        