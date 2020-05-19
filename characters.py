import pygame as game

#motion can 
class character:
    def __init__(self,widthOfWindow,heightOfWindow):
        self.widthOfWindow= widthOfWindow
        self.heightOfWindow = heightOfWindow
        self.width = 75
        self.height = 150
        self.x = 10
        self.y = heightOfWindow - self.height
        self.dx = 10
        self.dy = 50
        self.movingRight = False
        self.movingLeft = False
        self.jumping = False

    def draw(self,master):
        self.fall()
        self.move()
        game.draw.rect(master,(255,0,0),(self.x,self.y,self.width,self.height))

    def move(self):
        if self.movingRight and self.x + self.width + self.dx < self.widthOfWindow:
            self.x += self.dx
        if self.movingLeft and self.x - self.dx > 0:
            self.x -= self.dx

    def jump(self):
        self.jumping = True

    def fall(self):
        if self.jumping:
            if self.y + self.height - self.dy <= self.heightOfWindow:
                self.y -= self.dy
                self.dy -= 3
            else:
                self.y = self.heightOfWindow - self.height
                self.dy = 50
                self.jumping = False