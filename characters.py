import pygame as game

#motion can 
class character(game.sprite.Sprite):
    def __init__(self,widthOfWindow,heightOfWindow,controller):
        game.sprite.Sprite.__init__(self)
        #width and heights
        self.widthOfWindow = widthOfWindow
        self.heightOfWindow = heightOfWindow
        self.width = 75
        self.height = 150
        #SPRITE SETUP
        # create a plain rectangle for the sprite image | THIS is WIDTH and HEIGHT
        self.image = game.Surface((self.width, self.height))
        self.image.fill((255,0,0))
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # center the sprite on the screen | THIS IS NOT X or Y, this is just the coordinates of the center
        self.rect.center = (50, 200)
        #Movement
        self.dx = 10
        self.dy = 0
        self.colliFromHori = False
        self.somethingUnder = False
        self.gravity = 3
        self.falling = True

        self.controller = controller
        self.frameLag = 0

    def tick(self):
        if self.frameLag > 0:
            self.rect.x += self.dx
        else:
            self.dx = 10

    def somethingUnderTrue(self):
        self.somethingUnder = True
        self.dy = 0
    
    def notSomethingUnder(self):
        self.somethingUnder = False

    def update(self):
        self.fall()
        if self.frameLag == 0:
            self.dx = 10

    def moveH(self,key):
        #Right and left vary depending on the coordiantes, so right will be: x + width = right
        self.colliFromHori = False
        if key=="right" and self.rect.right + self.dx < self.widthOfWindow and self.frameLag == 0:
            self.rect.x += self.dx
            hits = game.sprite.spritecollide(self,self.controller.platforms,False)
            self.rect.x -= self.dx

            if hits:
                if hits[0].typeOf == "wall":
                    self.rect.x = hits[0].rect.left - self.width
                if hits[0].typeOf == "platform":
                    self.rect.x += self.dx
                    self.colliFromHori = True
            else:
                self.rect.x += self.dx

        if key=="left" and self.rect.x - self.dx > 0 and self.frameLag == 0:
            self.rect.x -= self.dx
            hits = game.sprite.spritecollide(self,self.controller.platforms,False)
            self.rect.x += self.dx
            if hits:
                if hits[0].typeOf == "wall":
                    self.rect.x = hits[0].rect.right
                if hits[0].typeOf == "platform":
                    self.rect.x -= self.dx
                    self.colliFromHori = True
            else:
                self.rect.x -= self.dx

    def fall(self):
        if not self.somethingUnder:
            self.rect.y -= self.dy
            if self.dy - self.gravity > -51:
                self.dy -= self.gravity
            else:
                self.dy = -51

            if self.dy <= 0:
                self.falling = True
        else:
            self.falling = False

        self.rect.y += 1
        hits = game.sprite.spritecollide(self,self.controller.platforms,False)
        self.rect.y -= 1
        if hits:
            if self.falling and self.rect.top < hits[0].rect.bottom and hits[0].typeOf == "platform" and not self.colliFromHori:
                self.rect.y = hits[0].rect.top - self.height
                self.somethingUnderTrue()

            if self.falling and self.rect.bottom < hits[0].rect.bottom and hits[0].typeOf == "wall":
                self.rect.y = hits[0].rect.top - self.height
                self.somethingUnderTrue()

            elif hits[0].typeOf == "floor":
                self.rect.y = hits[0].rect.top - self.height
                self.somethingUnderTrue()
        else:
            self.notSomethingUnder()

    def jump(self):
        if self.somethingUnder:
            self.somethingUnder = False
            self.dy = 51
        
    def wallJumpRight(self,master):
        self.rect.x += self.dx
        hits = game.sprite.spritecollide(self,self.controller.platforms,False)
        self.rect.x -= self.dx
        if hits and hits[0].typeOf == "wall":
            self.frameLag = 10
            self.dx = -16
            self.movingRight = False
            self.movingLeft = True
            self.somethingUnder = True
            self.jump()
            self.dy = 20

    def wallJumpLeft(self,master):
        self.rect.x -= self.dx
        hits = game.sprite.spritecollide(self,self.controller.platforms,False)
        self.rect.x += self.dx
        if hits and hits[0].typeOf == "wall":
            self.frameLag = 10
            self.dx = 16
            self.movingRight = True
            self.movingLeft = False
            self.somethingUnder = True
            self.jump()
            self.dy = 20