import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    # a class to represent a single alien in the fleet

    def __init__(self, ai_game):
        #initialize the alien and set its starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the alien image and set its rect attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 

        # store the alien's exact horizontal position
        self.x = float(self.rect.x)
    
    def check_edges(self):
        # return true if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.reigt or self.rect.left <=0:
            return True
    
    def _check_fleet_edges(self):
        #respond appropriately if any aliens have reached an edge
        for alien in self.alines.sprites():
            if alien. check_edges():
                self._change_fleet_direction()
            break
    
    def _change_fleet_direction(self):
        #drop the entire fleet and chagne the fleet's direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _update_aliens(self):
        # check if the fleet is at an edge, then update the postions of all aliens in the fleet.

        self._check_fleet_edges()
        self.aliens.update()
    
    def update(self):
        #move the alien to the right or left
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x =self.x

    def _upddate_bullets(self):
        # update position of bullets and get rid of old bullets
        # check for any bullets taht have hit aliens
        # if so , get rid of teh bullet and the alien
        collisions = pygame.sprite.groundcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            #destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
