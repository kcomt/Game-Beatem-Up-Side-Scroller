
import pygame as game
from os import path

class backGroundImage(game.sprite.Sprite):
    def __init__(self,widthOfWindow,heightOfWindow,controller):
        game.sprite.Sprite.__init__(self)
        self.controller = controller
        self.image = controller.backGroundImage.get_imageCustomScale(0, 0, 1200, 800,1200,800)
        self.rect = self.image.get_rect()
        self.rect.center = (600, 400)
        
    def moveBg(self):
        self.image = self.controller.backGroundImage.get_imageCustomScale(self.controller.character.rect.x/5, self.controller.character.rect.y/5, 1200, 800,1200,800)