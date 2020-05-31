import pygame as game

class healthBarBackColor(game.sprite.Sprite):
    def __init__(self,widthOfWindow,heightOfWindow,controller):
        game.sprite.Sprite.__init__(self)
        self.controller = controller
        self.widthOfWindow = widthOfWindow
        self.heightOfWindow = heightOfWindow
        self.image = game.Surface((600, 55))
        self.image.fill((150,150,150))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 850)

class healthBar(game.sprite.Sprite):
    def __init__(self,widthOfWindow,heightOfWindow,controller):
        game.sprite.Sprite.__init__(self)
        self.controller = controller
        self.widthOfWindow = widthOfWindow
        self.heightOfWindow = heightOfWindow
        self.frames = [self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 600, 100),
        self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 450, 100),
        self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 300, 100),
        self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 150, 100),
        self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 20, 100)]
        self.image = self.frames[1]
        #self.image.set_colorkey((25.1,50.2,0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.width/2 + 20, self.heightOfWindow-self.rect.height/2)

class inGameUIs:
    def __init__(self,widthOfWindow,heightOfWindow,controller):
        self.hbBackColor = healthBarBackColor(widthOfWindow,heightOfWindow,controller)
        self.healthBar = healthBar(widthOfWindow,heightOfWindow,controller)
        self.inGameGUIs = game.sprite.Group()
        self.inGameGUIs.add(self.hbBackColor)
        self.inGameGUIs.add(self.healthBar)

    def draw(self,master):
        self.inGameGUIs.draw(master)
