import pygame
from constants import *
from circleshape import *
from shot import *


class Player(CircleShape):
    def __init__(self, x, y, controls):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.controls = controls

    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[self.controls["left"]]:
            self.rotate(dt*-1)
        if keys[self.controls["right"]]:
            self.rotate(dt)
        if keys[self.controls["up"]]:
            self.move(dt)
        if keys[self.controls["down"]]:
            self.move(dt*-1)
        if keys[self.controls["shoot"]]:
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.timer <= 0:
            offset_distance = 50

            # Calculate the position for the shot
            offset = pygame.Vector2(0, offset_distance).rotate(self.rotation)
            bullet_position = self.position + offset

            bullet = Shot(bullet_position.x, bullet_position.y, SHOT_RADIUS)
            bullet.position = pygame.Vector2(bullet_position.x, bullet_position.y) 
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED 
            self.timer = PLAYER_SHOOT_COOLDOWN
        

                                        
