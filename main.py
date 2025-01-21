import pygame
import constants
import player
from constants import *

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    player_instance = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0, 0, 0))
        player_instance.draw(screen)
        player_instance.update(dt)
        pygame.display.flip()
        dt = game_clock.tick(60) /1000
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()