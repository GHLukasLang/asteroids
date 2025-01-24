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
    
    
    ########NEW STUFF
    # Player 1 controls (arrow keys and spacebar)
    player1_controls = {
        'left': pygame.K_LEFT,
        'right': pygame.K_RIGHT,
        'up': pygame.K_UP,
        "down": pygame.K_DOWN,
        'shoot': pygame.K_RCTRL
    }
    
    # Player 2 controls (WASD and Enter for shooting)
    player2_controls = {
        'left': pygame.K_a,
        'right': pygame.K_d,
        'up': pygame.K_w,
        "down": pygame.K_s,
        'shoot': pygame.K_SPACE
    }
    
    player1 = Player(SCREEN_WIDTH/4, SCREEN_HEIGHT / 2, player1_controls)
    player2 = Player(3*SCREEN_WIDTH/4, SCREEN_HEIGHT / 2, player2_controls)
    ##########################

    #player_1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT)
    #player_2 = Player(SCREEN_WIDTH, SCREEN_HEIGHT /2)
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
            if roids.collision(player1) or roids.collision(player2):
                print("Game over!")
                return
        
        #check for player-player-collisions
        if player1.collision(player2):
            print("Game over!")
            return
        if player2.collision(player1):
            print("Game over!")
            return


        #check for bullet-asteroid-collisions, remove bullet, split asteroid
        for asteroid in asteroids:    
            for bullet in shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()
        
        ##doesnt work yet! bullets overlap with the shooting player. solve by spawning shots outside of player-collision box?
        for bullet in shots:
            if bullet.collision(player1) or bullet.collision(player2):
                print("Game over!")
                return

        #redraw everything
        for drawables in drawable:
            drawables.draw(screen)
        
        #make the changes visible
        pygame.display.flip()



if __name__ == "__main__":
    main()

    