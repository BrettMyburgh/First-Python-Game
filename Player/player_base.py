import pygame

class player:

    player_pos = pygame.Vector2(0,0)
    screen = pygame.display
    stage_rect = pygame.Rect(player_pos.x, player_pos.y,30,30)


    def __init__ (self, startpos, screen):
        self.player_pos= startpos
        self.screen = screen

    def add_stage(self,screen):
        body_color = 15,200,50
        self.stage_rect.center = self.player_pos
        pygame.draw.rect(screen, body_color,self.stage_rect)
        return screen
    
    def get_player_rect(self):
        return self.stage_rect