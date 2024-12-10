import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *



def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

   
    ##########GROUPS AND CONTAINERS##########

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)

    AsteroidField.containers = (updateable)


    ##########INITAL VARIABLES##########

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT /2)
    field = AsteroidField()


    ##########WHILE LOOP##########
    
    while True:
        #enables to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #setup deltatime to a limit of 60 fps
        dt = clock.tick(60) / 1000   

        #fill the screen black
        screen.fill("black")

        #update movements etc
        for updateables in updateable:
            updateables.update(dt)

        #check for player-asteroid-collisions
        for roids in asteroids:
            if roids.collision(player):
                print("Game over!")
                return
        
        #check for bullet-asteroid-collisions, remove bullet, split asteroid
        for asteroid in asteroids:    
            for bullet in shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()

        #redraw everything
        for drawables in drawable:
            drawables.draw(screen)
        
        #make the changes visible
        pygame.display.flip()



if __name__ == "__main__":
    main()

    