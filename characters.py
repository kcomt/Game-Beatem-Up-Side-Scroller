import pygame as game

#motion can 
class character(game.sprite.Sprite):
    def __init__(self,widthOfWindow,heightOfWindow):
        game.sprite.Sprite.__init__(self)
        self.widthOfWindow = widthOfWindow
        self.heightOfWindow = heightOfWindow
        self.width = 75
        self.height = 150
        # create a plain rectangle for the sprite image | THIS is WIDTH and HEIGHT
        self.image = game.Surface((self.width, self.height))
        self.image.fill((255,0,0))
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # center the sprite on the screen | THIS IS NOT X or Y, this is just the coordinates of the center
        self.rect.center = (50, 50)
        self.dx = 10
        self.dy = 0
        self.movingRight = False
        self.movingLeft = False
        self.somethingUnder = False
        self.gravity = 3

    def somethingUnderTrue(self):
        self.somethingUnder = True
        self.dy = 0
    
    def notSomethingUnder(self):
        self.somethingUnder = False

    def update(self):
        self.fall()
        self.move()
        
    def move(self):
        #Right and left vary depending on the coordiantes, so right will be: x + width = right
        if self.movingRight and self.rect.right + self.dx < self.widthOfWindow:
            self.rect.x += self.dx
        if self.movingLeft and self.rect.x - self.dx > 0:
            self.rect.x -= self.dx

    def jump(self):
        if self.somethingUnder:
            self.somethingUnder = False
            self.dy = 50

    def fall(self):
        if not self.somethingUnder:
            self.rect.y -= self.dy
            self.dy -= 3