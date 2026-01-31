import pygame
from Player import player_base
from Items import item_base

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
delta = 0

player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
player = player_base.player(player_pos, screen)

item = item_base.item(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    bgcolor = 170,170,170
    screen.fill(bgcolor)
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

    player_rec = player.get_player_rect()

    item.check_colide(player_rec, screen)

    pygame.display.flip()

    delta = clock.tick(60) / 1000

pygame.quit()