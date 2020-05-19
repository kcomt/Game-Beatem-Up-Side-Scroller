import pygame as game
class structure(game.sprite.Sprite):
    def __init__(self,width,height,x,y):
        game.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        # create a plain rectangle for the sprite image | THIS is WIDTH and HEIGHT
        self.image = game.Surface((self.width, self.height))
        self.image.fill((0,255,0))
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # center the sprite on the screen | THIS IS NOT X or Y, this is just the coordinates of the center
        self.rect.center = (x, y)