import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # a class to manage bullets fired from the ship

    def __init__(self,ai_game):
        #create a bullet object at the ship's current position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
    
        # create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settins.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullet's position as a decimal value
        self.y = folat(self.rect.y)
    
    def update(self):
        #move the bullet up the screen
        #update the decimal postion of teh bullet

        self.y -= self.settings.bullet_speed
        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        #draw the bullet to the screen
        pygame.draw.rect(self.screen,self.color,self.rect)