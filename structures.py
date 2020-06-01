import pygame as game
from os import path

class structure(game.sprite.Sprite):
    def __init__(self,width,height,x,y,typeOf):
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
        self.typeOf = typeOf


class listOfStructures:
    def __init__(self):
        self.dir = path.dirname(__file__)
        txtDir = path.join(self.dir,'maps')
        self.text = []
        with open(path.join(txtDir,"map1.txt"), 'r') as f:
            for line in f:
                self.text.append(line)
        self.arr = []
        for i in self.text: 
            self.x = i.split("\n")
            self.arr.append(self.x[0])

        self.structures = game.sprite.Group()

    def createPlatforms(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                if self.arr[i][j] == "f":
                    structureObj = structure(50,100,25+j*50,50+i*100,"floor")
                    self.structures.add(structureObj)
                elif self.arr[i][j] == "w":
                    structureObj = structure(50,100,25+j*50,50+i*100,"wall")
                    self.structures.add(structureObj)
                elif self.arr[i][j] == "p":
                    structureObj = structure(50,100,25+j*50,50+i*100,"platform")
                    self.structures.add(structureObj)

class Camera:
    def __init__(self, width, height):
        self.camera = game.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(1200 / 2)
        y = -target.rect.y + int(1000 / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - 1200), x)  # right
        y = max(-(self.height - 1000), y)  # bottom
        self.camera = game.Rect(x, y, self.width, self.height)