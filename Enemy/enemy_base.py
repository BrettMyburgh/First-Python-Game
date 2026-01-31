import pygame
import random

class enemy:
    enemy_pos = pygame.Vector2(0,0)
    stage_rect = pygame.Rect(enemy_pos.x, enemy_pos.y,30,30)

    def __init__(self, screen):
        self.enemy_pos = pygame.Vector2(random.randint(0,screen.width - 50), random.randint(0,screen.height - 50))

    def add_enemy(self, screen):
        body_color = 200,15,50
        self.stage_rect.center = self.enemy_pos
        pygame.draw.rect(screen, body_color,self.stage_rect)
        return screen
    
    def move_enemy(self, apple_rect, delta):
        dif_x = self.enemy_pos.x - apple_rect.x
        x_speed = min(abs(dif_x),250* delta)
        if dif_x > 0:
            self.enemy_pos.x -= x_speed 
        elif dif_x < 0:
            self.enemy_pos.x += x_speed
        dif_y = self.enemy_pos.y - apple_rect.y
        y_speed = min(abs(dif_y),250* delta)
        if dif_y > 0:
            self.enemy_pos.y -= y_speed
        elif dif_y < 0:
            self.enemy_pos.y += y_speed
    
    def get_player_rect(self):
        return self.stage_rect