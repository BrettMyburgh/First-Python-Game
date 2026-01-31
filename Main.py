import pygame
from Player import player_base
from Items import item_base
from Enemy import enemy_base

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
delta = 0

player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
player = player_base.player(player_pos, screen)

enemy = enemy_base.enemy(screen)

item = item_base.item(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bgcolor = 170,170,170
    screen.fill(bgcolor)
    enemy.add_enemy(screen)
    player.add_stage(screen)
    item.add_item(screen)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.player_pos.y -= 300 * delta
    if keys[pygame.K_s]:
        player.player_pos.y += 300 * delta
    if keys[pygame.K_a]:
        player.player_pos.x -= 300 * delta
    if keys[pygame.K_d]:
        player.player_pos.x += 300 * delta

    enemy.move_enemy(item.get_apple_pos(),delta)

    player_rec = player.get_player_rect()
    enemy_rec = enemy.get_player_rect()

    item.check_colide(player_rec, enemy_rec, screen)

    pygame.display.flip()

    delta = clock.tick(60) / 1000

pygame.quit()