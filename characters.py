import pygame as game

class Spritesheet:
    # utility class for loading and parsing spritesheets
    def __init__(self, filename):
        self.spritesheet = game.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height):
        # grab an image out of a larger spritesheet
        image = game.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = game.transform.scale(image, (width*2, height*2))
        return image

#motion can 
class character(game.sprite.Sprite):
    def __init__(self,widthOfWindow,heightOfWindow,controller):
        game.sprite.Sprite.__init__(self)
        self.controller = controller
        #width and heights
        self.widthOfWindow = widthOfWindow
        self.heightOfWindow = heightOfWindow
        # center the sprite on the screen | THIS IS NOT X or Y, this is just the coordinates of the center
        self.animation = "standing"
        self.frames = [self.controller.spritesheet.get_image(17, 2182, 38, 60),
        self.controller.spritesheet.get_image(65, 2181, 38, 61),
        self.controller.spritesheet.get_image(113, 2180, 39, 62),
        self.controller.spritesheet.get_image(161, 2180, 39, 62),
        self.controller.spritesheet.get_image(209, 2180, 39, 62),
        self.controller.spritesheet.get_image(257, 2181, 38, 61)]

        self.image = self.frames[0]
        self.image.set_colorkey((25.1,50.2,0))
        self.rect = self.image.get_rect()
        self.rect.center = (50, 200)
        self.setMovementUp()
        self.animationLag = 0
        self.indexAnimation = 0
        self.currentMove = "standing"
    
        self.lastMoveRight = True
        self.lastDirection = "right"
        self.gravityX = 0

    def setMovementUp(self):
        #Movement
        self.dx = 10
        self.dy = 0
        self.colliFromHori = False
        self.somethingUnder = False
        self.gravity = 3
        self.falling = True
        self.frameLag = 0

    def setSpriteMovement(self,animation,direction):
        if animation == "standing":
            
            if direction == "right":
                self.frames = [self.controller.spritesheet.get_image(17, 2182, 38, 60),
                self.controller.spritesheet.get_image(65, 2181, 38, 61),
                self.controller.spritesheet.get_image(113, 2180, 39, 62),
                self.controller.spritesheet.get_image(161, 2180, 39, 62),
                self.controller.spritesheet.get_image(209, 2180, 39, 62),
                self.controller.spritesheet.get_image(257, 2181, 38, 62)]
            else:
                self.frames = [game.transform.flip(self.controller.spritesheet.get_image(17, 2182, 38, 60), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(65, 2181, 38, 61), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(113, 2180, 39, 62), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(161, 2180, 39, 62), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(209, 2180, 39, 62), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(257, 2181, 38, 62), True, False)]

        elif animation == "moving":
            if direction == "right":
                self.frames = [self.controller.spritesheet.get_image(11, 3408, 62, 40),
                self.controller.spritesheet.get_image(82, 3409, 58, 38),
                self.controller.spritesheet.get_image(144, 3405, 61, 42),
                self.controller.spritesheet.get_image(213, 3406, 58, 43),
                self.controller.spritesheet.get_image(277, 3411, 59, 38)]

            else:
                self.frames = [game.transform.flip(self.controller.spritesheet.get_image(11, 3408, 62, 40), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(82, 3409, 58, 38), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(144, 3405, 61, 42), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(213, 3406, 58, 43), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(277, 3411, 59, 38), True, False)]

        if animation != self.currentMove:
            self.animationLag = 5
            self.indexAnimation = 0
        elif self.lastDirection != direction:
            self.animationLag = 5
            self.indexAnimation = 0

        self.currentMove = animation
        self.lastDirection = direction

    def setAnimation(self):
        if self.indexAnimation < len(self.frames):
            self.image = self.frames[self.indexAnimation]
            auxRect = self.image.get_rect()
            if self.rect.height > auxRect.height:
                self.rect.y += self.rect.height - auxRect.height
            elif self.rect.height < auxRect.height:
                self.rect.y -= auxRect.height - self.rect.height
            #if self.rect.width > auxRect.width:

            self.rect.height = auxRect.height
            self.rect.width = auxRect.width
            self.indexAnimation += 1
        else:
            self.indexAnimation = 0

    def tick(self):
        if self.frameLag > 0:
            if self.dx < 20 and self.dx > -20:
                self.dx += self.gravityX
            self.rect.x += self.dx
            self.frameLag -= 1
        else:
            self.dx = 10

        if self.animationLag < 4:
            self.animationLag += 1
        else:
            self.setAnimation()
            self.animationLag = 0

    def somethingUnderTrue(self):
        self.somethingUnder = True
        self.dy = 0
        self.gravity = 3
    
    def notSomethingUnder(self):
        self.somethingUnder = False

    def update(self):
        self.fall()

    def moveH(self,key):
        #Right and left vary depending on the coordiantes, so right will be: x + width = right
        self.colliFromHori = False
        if key=="right" and self.rect.right + self.dx < self.widthOfWindow and self.frameLag == 0:
            self.rect.x += self.dx
            hits = game.sprite.spritecollide(self,self.controller.platforms,False)
            self.rect.x -= self.dx

            self.setSpriteMovement("moving","right")

            if hits:
                if hits[0].typeOf == "wall":
                    self.rect.x = hits[0].rect.left - self.rect.width
                if hits[0].typeOf == "platform":
                    self.rect.x += self.dx
                    self.colliFromHori = True
            else:
                self.rect.x += self.dx

        elif key=="left" and self.rect.x - self.dx > 0 and self.frameLag == 0:
            self.rect.x -= self.dx
            hits = game.sprite.spritecollide(self,self.controller.platforms,False)
            self.rect.x += self.dx

            self.setSpriteMovement("moving","left")

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
            if self.dy - self.gravity > -42:
                self.dy -= self.gravity
            else:
                self.dy = -42

            if self.dy <= 0:
                self.falling = True
        else:
            self.falling = False

        self.rect.y += 1
        hits = game.sprite.spritecollide(self,self.controller.platforms,False)
        self.rect.y -= 1
        if hits:
            if self.falling and self.rect.top < hits[0].rect.bottom and hits[0].typeOf == "platform" and not self.colliFromHori:
                self.rect.y = hits[0].rect.top - self.rect.height
                self.somethingUnderTrue()

            if self.falling and self.rect.bottom < hits[0].rect.bottom and hits[0].typeOf == "wall":
                self.rect.y = hits[0].rect.top - self.rect.height
                self.somethingUnderTrue()

            elif hits[0].typeOf == "floor":
                self.rect.y = hits[0].rect.top - self.rect.height
                self.somethingUnderTrue()
        else:
            self.notSomethingUnder()

    def jump(self):
        if self.somethingUnder:
            self.somethingUnder = False
            self.dy = 42
            self.gravity = 3

    def wallJumpRight(self,master):
        self.rect.x += self.dx
        hits = game.sprite.spritecollide(self,self.controller.platforms,False)
        self.rect.x -= self.dx
        if hits and hits[0].typeOf == "wall":
            self.frameLag = 20
            self.gravityX = -2
            self.dx = 0
            self.movingRight = False
            self.movingLeft = True
            self.somethingUnder = True
            self.setSpriteMovement("moving","left")
            self.jump()
            self.dy = 30
            

    def wallJumpLeft(self,master):
        self.rect.x -= self.dx
        hits = game.sprite.spritecollide(self,self.controller.platforms,False)
        self.rect.x += self.dx
        if hits and hits[0].typeOf == "wall":
            self.frameLag = 15
            self.gravityX = 2
            self.dx = 0
            self.movingRight = True
            self.movingLeft = False
            self.somethingUnder = True
            self.setSpriteMovement("moving","right")
            self.jump()
            self.dy = 30
            self.gravity = 2