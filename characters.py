import pygame as game

class animationLag:
    def __init__(self):
        self.type = None
        self.amount = 0
        self.interval = 0
        self.threshold = 0
        self.animationDx = 0
        self.animationDy = 0
        self.xAcceleration = 0
        self.xLimit = 0
        self.invisibilityFrames = 0
        
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
        self.rect.center = (100, 100)
        self.setMovementUp()
        self.health = 10
        self.newHealth = 10
        
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
        self.animationLagObj.xAcceleration = 0
        self.animationLagObj.animationDx = 0

    def somethingUnderTrue(self):
        self.wallJumpLag = 0
        self.somethingUnder = True
        self.dy = 0
        self.gravity = 3
        if self.animationLagObj.type == "air":
            self.animationLagObj.amount = 0

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

        elif animation == "crouching":
            if direction == "right":
                self.frames = [self.controller.spritesheet.get_image(12, 1083, 58, 37)]
            else:
                self.frames = [game.transform.flip(self.controller.spritesheet.get_image(12, 1083, 58, 37), True, False)]

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
            else:
                self.frames = [game.transform.flip(self.controller.spritesheet.get_image(14, 1488, 45, 58), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(108, 1473, 43, 68), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(215, 1478, 71, 65), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(312, 1492, 79, 53), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(405, 1494, 60, 58), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(500, 1494, 45, 60), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(581, 1495, 59, 53), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(677, 1494, 57, 54), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(775, 1491, 56, 51), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(880, 1496, 42, 41), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(976, 1492, 40, 46), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(1074, 1489, 39, 53), True, False)]

        elif animation == "neutralDown":
            if direction == "right":
                self.frames = [self.controller.spritesheet.get_image(116, 1089, 57, 33),
                self.controller.spritesheet.get_image(215, 1086, 50, 39),
                self.controller.spritesheet.get_image(319, 1085, 64, 37),
                self.controller.spritesheet.get_image(421, 1087, 92, 34),
                self.controller.spritesheet.get_image(522, 1087, 94, 35),
                self.controller.spritesheet.get_image(623, 1087, 84, 34),
                self.controller.spritesheet.get_image(724, 1088, 74, 33),
                self.controller.spritesheet.get_image(825, 1088, 67, 34),
                self.controller.spritesheet.get_image(927, 1088, 56, 34),
                self.controller.spritesheet.get_image(1027, 1088, 55, 34)]
            else:
                self.frames = [game.transform.flip(self.controller.spritesheet.get_image(116, 1089, 57, 33), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(215, 1086, 50, 39), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(319, 1085, 64, 37), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(421, 1087, 92, 34), True, False),
                game.transform.flip( self.controller.spritesheet.get_image(522, 1087, 94, 35), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(623, 1087, 84, 34), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(724, 1088, 74, 33), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(825, 1088, 67, 34), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(927, 1088, 56, 34), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(1027, 1088, 55, 34), True, False)]

        elif animation == "downAir":
            if direction == "right":
                self.frames = [self.controller.spritesheet.get_image(44, 396, 58, 52),
                self.controller.spritesheet.get_image(146, 385, 48, 71),
                self.controller.spritesheet.get_image(257, 397, 42, 55),
                self.controller.spritesheet.get_image(358, 402, 73, 55),
                self.controller.spritesheet.get_image(462, 404, 45, 75),
                self.controller.spritesheet.get_image(555, 407, 54, 50),
                self.controller.spritesheet.get_image(641, 403, 79, 53),
                self.controller.spritesheet.get_image(760, 381, 69, 71),
                self.controller.spritesheet.get_image(892, 380, 38, 71),
                self.controller.spritesheet.get_image(995, 380, 48, 75),
                self.controller.spritesheet.get_image(1089, 385, 59, 70),
                self.controller.spritesheet.get_image(1185, 383, 67, 73),
                self.controller.spritesheet.get_image(1307, 393, 46, 65),
                self.controller.spritesheet.get_image(1417, 391, 32, 66)]
            else:
                self.frames = [game.transform.flip(self.controller.spritesheet.get_image(44, 396, 58, 52), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(146, 385, 48, 71), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(257, 397, 42, 55), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(358, 402, 73, 55), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(462, 404, 45, 75), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(555, 407, 54, 50), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(641, 403, 79, 53), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(760, 381, 69, 71), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(892, 380, 38, 71), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(995, 380, 48, 75), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(1089, 385, 59, 70), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(1185, 383, 67, 73), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(1307, 393, 46, 65), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(1417, 391, 32, 66), True, False)]

        elif animation == "neutral":
            if direction == "right":
                self.frames = [self.controller.spritesheet.get_image(16, 837, 38, 54),
                self.controller.spritesheet.get_image(117, 838, 38, 53),
                self.controller.spritesheet.get_image(224, 841, 82, 49),
                self.controller.spritesheet.get_image(324, 844, 91, 45),
                self.controller.spritesheet.get_image(424, 825, 52, 64),
                self.controller.spritesheet.get_image(516, 853, 61, 39),
                self.controller.spritesheet.get_image(627, 853, 51, 39),
                self.controller.spritesheet.get_image(730, 851, 48, 42),
                self.controller.spritesheet.get_image(834, 841, 52, 51),
                self.controller.spritesheet.get_image(922, 832, 52, 59),
                self.controller.spritesheet.get_image(1022, 831, 48, 60)]
            else:
                self.frames = [game.transform.flip(self.controller.spritesheet.get_image(16, 837, 38, 54), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(117, 838, 38, 53), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(224, 841, 82, 49), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(324, 844, 91, 45), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(424, 825, 52, 64), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(516, 853, 61, 39), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(627, 853, 51, 39), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(730, 851, 48, 42), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(834, 841, 52, 51), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(922, 832, 52, 59), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(1022, 831, 48, 60), True, False)]
        
        elif animation == "flinch":
            if direction == "right":
                self.frames = [self.controller.spritesheet.get_image(18, 4218, 43, 60),
                self.controller.spritesheet.get_image(72, 4216, 37, 62),
                self.controller.spritesheet.get_image(122, 4218, 34, 60),
                self.controller.spritesheet.get_image(167, 4219, 38, 59),
                self.controller.spritesheet.get_image(218, 4219, 35, 58),
                self.controller.spritesheet.get_image(261, 4218, 48, 59),
                self.controller.spritesheet.get_image(318, 4217, 42, 60)]
            else:
                self.frames = [game.transform.flip(self.controller.spritesheet.get_image(18, 4218, 43, 60), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(72, 4216, 37, 62), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(122, 4218, 34, 60), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(167, 4219, 38, 59), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(218, 4219, 35, 58), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(261, 4218, 48, 59), True, False),
                game.transform.flip(self.controller.spritesheet.get_image(318, 4217, 42, 60), True, False)]

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
        if self.animationLagObj.interval < self.animationLagObj.threshold:
            self.animationLagObj.interval += 1
        else:
            self.setAnimation()
            self.animationLagObj.interval = 0
            if self.newHealth < self.health:
                self.health -= 1
        if self.animationLagObj.amount > 0:
            self.animationMovement()
            self.animationLagObj.amount -= 1
        else:
            self.animationLagObj.type = None
            self.animationLagObj.threshold = 4
            self.animationLagObj.xAcceleration = 0
        if self.animationLagObj.invisibilityFrames > 0:
            self.animationLagObj.invisibilityFrames -= 1
            
    def animationMovement(self):
        if self.rect.x + self.animationLagObj.animationDx > 0:
                self.rect.x += self.animationLagObj.animationDx
                if -1*self.animationLagObj.xLimit < self.animationLagObj.animationDx and self.animationLagObj.animationDx < self.animationLagObj.xLimit:
                    self.animationLagObj.animationDx += self.animationLagObj.xAcceleration
        else:
            self.rect.x = 0
        hits = game.sprite.spritecollide(self,self.controller.platforms,False)
        if hits and hits[0].typeOf == "wall":
                if self.lastDirection == "right":
                    self.rect.x = hits[0].rect.left - self.rect.width
                elif self.lastDirection == "left":
                    self.rect.x = hits[0].rect.right

    def moveH(self,key):
        if self.animationLagObj.type != "ground" and self.animationLagObj.type != "wallJump":
            self.colliFromHori = False
            if self.animationLagObj.type != "air":
                if self.somethingUnder:
                    self.setSpriteMovement("moving",key)
                    self.getFrameWidthAndHeight()
                else:
                    self.setSpriteMovement(self.currentMove,key)
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
        if self.animationLagObj.amount == 0:
            if direction == "right":
                self.rect.x += self.dx
                hits = game.sprite.spritecollide(self,self.controller.platforms,False)
                self.rect.x -= self.dx
                if hits and hits[0].typeOf == "wall":
                    self.animationLagObj.type = "wallJump"
                    self.animationLagObj.amount = 17
                    self.animationLagObj.animationDx = 0
                    self.animationLagObj.xAcceleration = -2
                    self.animationLagObj.xLimit = 17
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
                    self.animationLagObj.type = "wallJump"
                    self.animationLagObj.amount = 17
                    self.animationLagObj.animationDx = 0
                    self.animationLagObj.xAcceleration = 2
                    self.animationLagObj.xLimit = 17
                    self.movingRight = False
                    self.movingLeft = True
                    self.somethingUnder = True
                    self.setSpriteMovement("moving","right")
                    self.jump()
                    self.dy = 36
    
    def fowardDash(self,direction):
        if self.animationLagObj.amount == 0:
            if direction == "right":
                self.animationLagObj.animationDx = 8
                self.animationLagObj.type = "ground"
                self.animationLagObj.threshold = 2
                self.animationLagObj.amount = 15*self.animationLagObj.threshold
                self.animationLagObj.invisibilityFrames = self.animationLagObj.amount
                self.setSpriteMovement("fowardDash",self.lastDirection)

            elif direction == "left":
                self.animationLagObj.animationDx = -8
                self.animationLagObj.type = "ground"
                self.animationLagObj.threshold = 2
                self.animationLagObj.amount = 15*self.animationLagObj.threshold
                self.animationLagObj.invisibilityFrames = self.animationLagObj.amount
                self.setSpriteMovement("fowardDash",self.lastDirection)
    
    def fowardAir(self,direction):
        if self.animationLagObj.amount == 0:
            if direction == "right":
                self.animationLagObj.animationDx = 0
                self.animationLagObj.type = "air"
                self.animationLagObj.threshold = 2
                self.animationLagObj.amount = 12*self.animationLagObj.threshold
                self.animationLagObj.invisibilityFrames = self.animationLagObj.amount
                self.setSpriteMovement("fowardAir",self.lastDirection)

            if direction == "left":
                self.animationLagObj.animationDx = 0
                self.animationLagObj.type = "air"
                self.animationLagObj.threshold = 2
                self.animationLagObj.amount = 12*self.animationLagObj.threshold
                self.animationLagObj.invisibilityFrames = self.animationLagObj.amount
                self.setSpriteMovement("fowardAir",self.lastDirection)
    
    def neutralDown(self):
         if self.animationLagObj.amount == 0:
            self.animationLagObj.animationDx = 0
            self.animationLagObj.type = "ground"
            self.animationLagObj.threshold = 2
            self.animationLagObj.amount = 10*self.animationLagObj.threshold
            self.animationLagObj.invisibilityFrames = self.animationLagObj.amount
            self.setSpriteMovement("neutralDown",self.lastDirection)

    def downAir(self):
         if self.animationLagObj.amount == 0:
            self.animationLagObj.animationDx = 0
            self.animationLagObj.type = "air"
            self.animationLagObj.threshold = 2
            self.animationLagObj.amount = 14*self.animationLagObj.threshold
            self.animationLagObj.invisibilityFrames = self.animationLagObj.amount
            self.setSpriteMovement("downAir",self.lastDirection)
 
    def neutral(self):
        if self.animationLagObj.amount == 0:
            self.animationLagObj.animationDx = 0
            self.animationLagObj.type = "ground"
            self.animationLagObj.threshold = 2
            self.animationLagObj.amount = 11*self.animationLagObj.threshold
            self.animationLagObj.invisibilityFrames = self.animationLagObj.amount
            self.setSpriteMovement("neutral",self.lastDirection)

    def takeHit(self,amount):
        if self.animationLagObj.invisibilityFrames == 0:
            self.animationLagObj.animationDx = 0
            self.animationLagObj.type = "ground"
            self.animationLagObj.threshold = 3
            self.animationLagObj.amount = 7*self.animationLagObj.threshold
            self.animationLagObj.invisibilityFrames = self.animationLagObj.amount+15
            self.newHealth = self.health - amount
            self.setSpriteMovement("flinch",self.lastDirection)
