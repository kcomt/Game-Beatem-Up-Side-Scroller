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
        self.frames =[self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 10, 100),
        self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 60, 100),
        self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 120, 100),
        self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 180, 100),
        self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 240, 100),
        self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 300, 100),
        self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 360, 100),
        self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 420, 100),
        self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 480, 100),
        self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 540, 100),
        self.controller.healthBarImage.get_imageCustomScale(270, 300, 600, 216, 600, 100)]

        self.image = self.frames[len(self.frames)-1]
        #self.image.set_colorkey((25.1,50.2,0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.width/2 + 20, self.heightOfWindow-self.rect.height/2)

    def setHealth(self,healthIndex):
        if healthIndex >= 0 and healthIndex <= 10:
            self.image = self.frames[healthIndex]

class inGameUIs:
    def __init__(self,widthOfWindow,heightOfWindow,controller):
        self.hbBackColor = healthBarBackColor(widthOfWindow,heightOfWindow,controller)
        self.healthBar = healthBar(widthOfWindow,heightOfWindow,controller)
        self.inGameGUIs = game.sprite.Group()
        self.inGameGUIs.add(self.hbBackColor)
        self.inGameGUIs.add(self.healthBar)

    def draw(self,master):
        self.inGameGUIs.draw(master)

    def setHealth(self,healthIndex):
        self.healthBar.setHealth(healthIndex)