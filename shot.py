import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2()

    def draw(self, screen):
        pygame.draw.circle(screen, "green", (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        forward = self.velocity * dt
        self.position += forward
