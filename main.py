import pygame
import constants
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()