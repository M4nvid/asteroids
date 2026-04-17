import pygame
import random
from circleshape import *
from constants import *
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, width = LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_velocity = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        self.smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid = Asteroid(self.position, self.position, self.smaller_radius)
        new_asteroid2 = Asteroid(self.position, self.position, self.smaller_radius)
        new_asteroid.velocity = new_velocity * 1.2
        new_asteroid2.velocity = new_velocity2 * 1.2
