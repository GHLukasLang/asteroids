import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *


## IN ORDER TO HAVE FULLSCREEN
def set_fullscreen_mode():
    # get the current resultion
    info = pygame.display.Info()
    screen_width, screen_height = info.current_w, info.current_h
    return pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)



def main():
    pygame.init()

   
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
    screen = set_fullscreen_mode()
   
    
    
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

    #player color
    player_1_color = "red"
    player_2_color = "blue"
    
    screen_width, screen_height = pygame.display.get_surface().get_size()  # Get the actual screen size

    player1 = Player(screen_width/4, screen_height / 2, player1_controls, player_1_color)
    player2 = Player(3*screen_width/4, screen_height / 2, player2_controls, player_2_color)
    ##########################

    
    field = AsteroidField(screen_width, screen_height)

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

    