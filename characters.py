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

class animationLag:
    def __init__(self):
        self.type = None
        self.amount = 0
        self.interval = 0
        self.threshold = 0

class character(game.sprite.Sprite):
    def __init__(self,widthOfWindow,heightOfWindow,controller):
        game.sprite.Sprite.__init__(self)
        self.controller = controller
        self.widthOfWindow = widthOfWindow
        self.heightOfWindow = heightOfWindow
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

    def setMovementUp(self):
        self.dx = 10
        self.dy = 0
        self.colliFromHori = False
        self.somethingUnder = False
        self.gravity = 3
        self.falling = True
        self.wallJumpLag = 0
        self.indexAnimation = 0
        self.currentMove = "standing"
        self.lastDirection = "right"
        self.gravityX = 0

        self.animationLagObj = animationLag()
        self.animationLagObj.amount = 0
        self.animationLagObj.interval = 0
        self.animationLagObj.threshold = 4

        self.animationDx = 0
        self.animationDy = 0

    def somethingUnderTrue(self):
        self.wallJumpLag = 0
        self.somethingUnder = True
        self.dy = 0
        self.gravity = 3
    
    def notSomethingUnder(self):
        self.somethingUnder = False

    def update(self):
        self.updateAnimation()
        self.fall()

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

        elif animation == "jumping":
            if direction == "right":
                self.frames = [self.controller.spritesheet.get_image(18, 2557, 36, 63),
                self.controller.spritesheet.get_image(67, 2558, 47, 62),
                self.controller.spritesheet.get_image(117, 2558, 51, 61),
                self.controller.spritesheet.get_image(170, 2560, 51, 59)]
            else:
                self.frames = [game.transform.flip(self.controller.spritesheet.get_image(18, 2557, 36, 63), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(67, 2558, 47, 62), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(117, 2558, 51, 61), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(170, 2560, 51, 59), True, False)]

        elif animation == "falling":
            if direction == "right":
                self.frames = [self.controller.spritesheet.get_image(18, 2630, 46, 57),
                self.controller.spritesheet.get_image(71, 2630, 46, 57)]
            else:
                self.frames = [game.transform.flip(self.controller.spritesheet.get_image(18, 2630, 46, 57), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(71, 2630, 46, 57), True, False)]

        elif animation == "fowardDash":
            if direction == "right":
                self.frames = [self.controller.spritesheet.get_image(23, 1664, 60, 35),
                self.controller.spritesheet.get_image(126, 1666, 68, 34),
                self.controller.spritesheet.get_image(228, 1664, 55, 36),
                self.controller.spritesheet.get_image(328, 1662, 61, 39),
                self.controller.spritesheet.get_image(427, 1662, 62, 41),
                self.controller.spritesheet.get_image(531, 1661, 52, 44),
                self.controller.spritesheet.get_image(638, 1663, 61, 38),
                self.controller.spritesheet.get_image(744, 1662, 90, 39),
                self.controller.spritesheet.get_image(850, 1663, 97, 38),
                self.controller.spritesheet.get_image(956, 1653, 91, 48),
                self.controller.spritesheet.get_image(1061, 1645, 55, 56),
                self.controller.spritesheet.get_image(1170, 1659, 48, 41),
                self.controller.spritesheet.get_image(1269, 1649, 48, 52),
                self.controller.spritesheet.get_image(1369, 1650, 65, 51),
                self.controller.spritesheet.get_image(1483, 1641, 44, 60)]
            else:
                self.frames = [game.transform.flip(self.controller.spritesheet.get_image(23, 1664, 60, 35), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(126, 1666, 68, 34), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(228, 1664, 55, 36), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(328, 1662, 61, 39), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(427, 1662, 62, 41), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(531, 1661, 52, 44), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(638, 1663, 61, 38), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(744, 1662, 90, 39), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(850, 1663, 97, 38), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(956, 1653, 91, 48), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(1061, 1645, 55, 56), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(1170, 1659, 48, 41), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(1269, 1649, 48, 52), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(1369, 1650, 65, 51), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(1483, 1641, 44, 60), True, False)]

        elif animation == "fowardAir":
            if direction == "right":
                self.frames = [self.controller.spritesheet.get_image(14, 1488, 45, 58),
                self.controller.spritesheet.get_image(108, 1473, 43, 68),
                self.controller.spritesheet.get_image(215, 1478, 71, 65),
                self.controller.spritesheet.get_image(312, 1492, 79, 53),
                self.controller.spritesheet.get_image(405, 1494, 60, 58),
                self.controller.spritesheet.get_image(500, 1494, 45, 60),
                self.controller.spritesheet.get_image(581, 1495, 59, 53),
                self.controller.spritesheet.get_image(677, 1494, 57, 54),
                self.controller.spritesheet.get_image(775, 1491, 56, 51),
                self.controller.spritesheet.get_image(880, 1496, 42, 41),
                self.controller.spritesheet.get_image(976, 1492, 40, 46),
                self.controller.spritesheet.get_image(1074, 1489, 39, 53)]

        if animation != self.currentMove:
            self.animationLagObj.interval = 5
            self.indexAnimation = 0
        elif self.lastDirection != direction:
            self.animationLagObj.interval = 5
            self.indexAnimation = 0

        self.currentMove = animation
        self.lastDirection = direction

    def getFrameWidthAndHeight(self):
        auxRect = self.image.get_rect()
        if self.rect.height > auxRect.height:
            self.rect.y += self.rect.height - auxRect.height
        elif self.rect.height < auxRect.height:
            self.rect.y -= auxRect.height - self.rect.height

        oldWidth = self.rect.width
        self.rect.width = auxRect.width
        self.rect.height = auxRect.height
        hits = game.sprite.spritecollide(self,self.controller.platforms,False)
        if self.lastDirection == "right":
            if hits and hits[0].typeOf == "wall":
                self.rect.x -= auxRect.width-oldWidth
        else:
            if oldWidth < self.rect.width:
                self.rect.x -= auxRect.width-oldWidth
            elif self.rect.width < oldWidth:
                self.rect.x += oldWidth-auxRect.width

    def setAnimation(self):
        if self.indexAnimation < len(self.frames):
            self.image = self.frames[self.indexAnimation]
            self.getFrameWidthAndHeight()
            self.indexAnimation += 1
        else:
            self.indexAnimation = 0

    def updateAnimation(self):
        if self.wallJumpLag > 0:
            if self.dx < 17 and self.dx > -17:
                self.dx += self.gravityX
            self.rect.x += self.dx
            self.wallJumpLag -= 1
        else:
            self.dx = 10
        if self.animationLagObj.interval < self.animationLagObj.threshold:
            self.animationLagObj.interval += 1
        else:
            self.setAnimation()
            self.animationLagObj.interval = 0
        if self.animationLagObj.amount > 0:
            self.animationMovement()
            self.animationLagObj.amount -= 1
        else:
            self.animationLagObj.threshold = 4

    def animationMovement(self):
        if self.rect.x + self.animationDx > 0:
                self.rect.x += self.animationDx
        else:
            self.rect.x = 0
        hits = game.sprite.spritecollide(self,self.controller.platforms,False)
        if hits and hits[0].typeOf == "wall":
                if self.lastDirection == "right":
                    print("YTERR")
                    self.rect.x = hits[0].rect.left - self.rect.width
                elif self.lastDirection == "left":
                    self.rect.x = hits[0].rect.right

    def moveH(self,key):
        if self.animationLagObj.amount == 0 and self.wallJumpLag == 0:
            self.colliFromHori = False
            if self.somethingUnder:
                self.setSpriteMovement("moving",key)
                self.getFrameWidthAndHeight()
            else:
                self.setSpriteMovement(self.lastDirection,key)
                self.getFrameWidthAndHeight()

            if key=="right" and self.rect.right + self.dx < self.widthOfWindow:
                self.rect.x += self.dx
                hits = game.sprite.spritecollide(self,self.controller.platforms,False)
                self.rect.x -= self.dx
                if hits:
                    if hits[0].typeOf == "wall":
                        self.rect.x = hits[0].rect.left - self.rect.width
                    if hits[0].typeOf == "platform":
                        self.rect.x += self.dx
                        self.colliFromHori = True
                else:
                    self.rect.x += self.dx
            elif key=="left" and self.rect.x - self.dx > 0:
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
            if self.dy - self.gravity > -42:
                self.dy -= self.gravity
            else:
                self.dy = -42
            if self.dy <= 0:
                self.falling = True
                if self.animationLagObj.amount == 0 or self.animationLagObj.type != "air":
                    self.setSpriteMovement("falling",self.lastDirection)
                #self.animationLag =  0
        else:
            self.falling = False
        self.rect.y += 1
        hits = game.sprite.spritecollide(self,self.controller.platforms,False)
        self.rect.y -= 1
        if hits:
            if self.falling and hits[0].typeOf == "platform" and not self.colliFromHori:
                if self.rect.bottom <= hits[0].rect.bottom:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    self.somethingUnderTrue()
                elif self.rect.top <= hits[0].rect.bottom and self.lastBottom < hits[0].rect.bottom:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    self.somethingUnderTrue()
            if self.falling and self.rect.bottom <= hits[0].rect.bottom and hits[0].typeOf == "wall":
                self.rect.y = hits[0].rect.top - self.rect.height
                self.somethingUnderTrue()
            elif hits[0].typeOf == "floor":
                self.rect.y = hits[0].rect.top - self.rect.height
                self.somethingUnderTrue()
        else:
            self.notSomethingUnder()
            self.lastBottom = self.rect.bottom

    def jump(self):
        if self.somethingUnder:
            self.somethingUnder = False
            self.dy = 42
            self.gravity = 3
            self.setSpriteMovement("jumping",self.lastDirection)

    def wallJump(self,direction):
        if direction == "right":
            self.rect.x += self.dx
            hits = game.sprite.spritecollide(self,self.controller.platforms,False)
            self.rect.x -= self.dx
            if hits and hits[0].typeOf == "wall":
                self.wallJumpLag = 17
                self.gravityX = -2
                self.dx = 0
                self.movingRight = False
                self.movingLeft = True
                self.somethingUnder = True
                self.setSpriteMovement("moving","left")
                self.jump()
                self.dy = 36
        else:
            self.rect.x -= self.dx
            hits = game.sprite.spritecollide(self,self.controller.platforms,False)
            self.rect.x += self.dx
            if hits and hits[0].typeOf == "wall":
                self.wallJumpLag = 17
                self.gravityX = 2
                self.dx = 0
                self.movingRight = True
                self.movingLeft = False
                self.somethingUnder = True
                self.setSpriteMovement("moving","right")
                self.jump()
                self.dy = 36
    
    def fowardDash(self,direction):
        if self.animationLagObj.amount == 0:
            if direction == "right":
                self.animationDx = 8
                self.animationLagObj.type = "ground"
                self.animationLagObj.threshold = 2
                self.animationLagObj.amount = 15*self.animationLagObj.threshold
                self.setSpriteMovement("fowardDash",self.lastDirection)

            elif direction == "left":
                self.animationDx = -8
                self.animationLagObj.type = "ground"
                self.animationLagObj.threshold = 2
                self.animationLagObj.amount = 15*self.animationLagObj.threshold
                self.setSpriteMovement("fowardDash",self.lastDirection)
    
    def fowardAir(self,direction):
        if self.animationLagObj.amount == 0:
            if direction == "right":
                self.animationDx = 0
                self.animationLagObj.type = "air"
                self.animationLagObj.threshold = 2
                self.animationLagObj.amount = 12*self.animationLagObj.threshold
                self.setSpriteMovement("fowardAir",self.lastDirection)