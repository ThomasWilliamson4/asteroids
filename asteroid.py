import pygame
import circleshape
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20,50)
        vector_1 = self.velocity.rotate(angle)
        vector_2 = self.velocity.rotate(-angle)
    
        self.radius -= constants.ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)

        asteroid_1.velocity = vector_1 * 1.2
        asteroid_2.velocity = vector_2 * 1.2

    

