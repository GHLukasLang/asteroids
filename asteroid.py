import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2() #can be empty as it is set by the spawn-method


    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        forward = self.velocity * dt
        self.position += forward

    def split(self):
        self.kill() #get rid of the asteroid, and DONT create a new one if it was a small one
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
        #create two smaller asteroids: 
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        for angle in [random_angle, -random_angle]:
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = self.velocity.rotate(angle) * 1.2
