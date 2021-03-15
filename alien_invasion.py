import sys
import pygame   

class AlienInvasion:
    # Overall class to manage game assets and behavior.

    def __init__(self):
        # initialize the background settings, and create game resources.
        pygame.init()

        # create a display window. 
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion") 

        # set the background color.
        self.bg_color = (230,230,230)

    def run_game(self):
        #Start the main loop for the game.
        while True:
            # watch for keyboard and moouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            
            # make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

