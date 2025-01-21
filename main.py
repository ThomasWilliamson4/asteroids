import pygame
import constants
from constants import *
from player import Player

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    game_clock = pygame.time.Clock()
    dt = 0
    player_instance = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #pygame.Surface.fill(screen, (0, 0, 0))
        #player_instance.draw(screen)
        #player_instance.update(dt)
        
        for obj in updatable:
            obj.update(dt)
        
        pygame.Surface.fill(screen, (0, 0, 0))
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) /1000


if __name__ == "__main__":
    main()