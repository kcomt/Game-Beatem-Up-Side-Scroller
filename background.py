
import pygame as game
from os import path

class backGroundImage(game.sprite.Sprite):
    def __init__(self,widthOfWindow,heightOfWindow,controller):
        game.sprite.Sprite.__init__(self)
        self.controller = controller
        self.image = controller.backGroundImage.get_imageCustomScale(200, 200, 1200, 800,1200,800)
        self.rect = self.image.get_rect()
        self.rect.center = (600, 400)
        
    def moveBg(self):
        y = self.controller.character.rect.bottom//15
        if self.controller.character.lastDirection == "right":
            x = self.controller.character.rect.x // 15
        else:
            x = self.controller.character.rect.right // 15
        self.image = self.controller.backGroundImage.get_imageCustomScale(x, y, 1200, 800,1200,800)