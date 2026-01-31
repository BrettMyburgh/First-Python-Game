import pygame
import sys
import random
from pathlib import Path


class item:
    pos = pygame.Vector2()
    script_dir = Path(__file__).parent

    def __init__(self, screen):
        self.pos = pygame.Vector2(random.randint(0,screen.get_width()), random.randint(0,screen.get_height()))

    def add_item(self, screen):
        apple = pygame.image.load(self.script_dir / "../Icons/apple.png")
        apple = pygame.transform.scale(apple, (10,10))
        applerect = apple.get_rect()
        screen.blit(apple, applerect)
        return screen