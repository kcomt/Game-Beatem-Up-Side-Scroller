import pygame as game

class healthBar(game.sprite.Sprite):
    def __init__(self,widthOfWindow,heightOfWindow,controller):
        game.sprite.Sprite.__init__(self)
        self.controller = controller
        self.widthOfWindow = widthOfWindow
        self.heightOfWindow = heightOfWindow
        self.frames = [self.controller.healthBarImage.get_imageCustomScale(54, 300, 1044, 216, 400, 100),
        self.controller.healthBarImage.get_imageCustomScale(54, 300, 817, 216, 400, 100),
        self.controller.healthBarImage.get_imageCustomScale(54, 300, 600, 216, 800, 200),
        self.controller.healthBarImage.get_imageCustomScale(54, 300, 415, 216, 800, 200),
        self.controller.healthBarImage.get_imageCustomScale(54, 300, 230, 216, 800, 200)]
        self.image = self.frames[0]
        #self.image.set_colorkey((25.1,50.2,0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.width/2, self.heightOfWindow-self.rect.height/2)