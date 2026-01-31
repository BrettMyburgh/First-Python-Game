import pygame

class player:

    player_pos = pygame.Vector2(0,0)
    screen = pygame.display

    def __init__ (self, startpos, screen):
        self.player_pos= startpos
        self.screen = screen

    def add_stage(self,screen):
        body_color = 15,200,50
        stage_rect = pygame.Rect(self.player_pos.x, self.player_pos.y,10,10)
        pygame.draw.rect(screen, body_color,stage_rect)
        return screen
    