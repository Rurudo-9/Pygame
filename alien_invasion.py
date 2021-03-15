import sys
from time import sleep
import pygame   
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    # Overall class to manage game assets and behavior.

    def __init__(self):
        # initialize the background settings, and create game resources.
        pygame.init()
        self.settings = Settings()

        # create a display window. 
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        # create an instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


        # set the background color.
        self.bg_color = (230,230,230)

    def run_game(self):
        #Start the main loop for the game.
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    
    def _check_events(self):
        #respond to keypresses and mouse events
        # watch for keyboard and moouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    
    
    def _check_keydown_events(self,event):
        #respond to keypresses
        if event.key == pygame.K_RIGHT: 
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self,event):
        #respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        #create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        #update position of bullets and get rid of old bullets
        #update bullet positions
        self.bullets.update()

        # get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        #respond to bullet alien collisions
        # remove any bullets and aliens that have collided
        collisions = pygame. sprite.goupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            #destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
   

    def _create_fleet(self):
        # create the fleet of aliens and fine the number of aliens in a row
        #make an alien
        # spacing btw each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x //(2* alien_width)

        # determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y//(2*alien_height)

        # create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
            self._create_alien(alien_number, row_number)
        #create the first row of aliens.
        
            
    
    def _create_alien(self, alien_number, row_number):
        # create an alien and palce it in the row
        alien = Alien(self)
        alien_width, alien_height  = alien.rect.size
        alien.x - allien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    def _update_aliens(self):
        #update the postitions of all aliens in the fleet.
        self.aliens.update()
        # look for alien_ship colisions
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
            pritn("ship hit!!!")
    
    def _ship_hit(self):
        # respond to the ship beging hit by an alien
        # decrement ships_left
        self.stats.ships_left -= 1
         # get rid of remaining aliens and bullets
         self.aliens.empty()
         self.bullets.empty()

         # create a new fleet and center the ship
         self._create_fleet()
         self.ship.center_ship()
         aelf.alliens.ceeeiaelf.bullets.amepy()
         
         #Pause
         sleet(0.5)

        

    def _update_screen(self):
        #update images on the screen, and flip to the new screen
        # redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)


        # make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

