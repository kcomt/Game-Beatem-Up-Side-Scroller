import pygame as game
from os import path

class structure(game.sprite.Sprite):
    def __init__(self,width,height,x,y,typeOf,controller,direction,mapNum):
        game.sprite.Sprite.__init__(self)
        if mapNum == 1:
            self.width = width
            self.height = height
            self.typeOf = typeOf
            if typeOf == "floor":
                self.image = controller.tileSheet.get_imageCustomScale(73, 82, 49, 20,self.width,self.height)
            elif typeOf == "platform":
                self.image = controller.tileSheet.get_imageCustomScale(138, 81, 90, 21,self.width,self.height)
            elif typeOf == "filler":
                self.image = controller.tileSheet.get_imageCustomScale(11, 8, 25, 50,self.width,self.height)
            elif typeOf == "ceiling":
                self.image = controller.tileSheet.get_imageCustomScale(111, 8, 25, 50,self.width,self.height)
            else:
                if direction == "right":
                    self.image = controller.tileSheet.get_imageCustomScale(112, 115, 22, 60,self.width,self.height)
                else:
                    self.image = game.transform.flip(controller.tileSheet.get_imageCustomScale(112, 115, 22, 60,self.width,self.height), True, False)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
        else:
            self.width = width
            self.height = height
            self.typeOf = typeOf
            if typeOf == "floor":
                self.image = controller.tileSheet.get_imageCustomScale(73, 82, 49, 20,self.width,self.height)
            elif typeOf == "platform":
                self.image = controller.tileSheet.get_imageCustomScale(138, 81, 90, 21,self.width,self.height)
            elif typeOf == "filler":
                self.image = controller.tileSheet.get_imageCustomScale(11, 8, 25, 50,self.width,self.height)
            elif typeOf == "ceiling":
                self.image = controller.tileSheet.get_imageCustomScale(111, 8, 25, 50,self.width,self.height)
            else:
                if direction == "right":
                    self.image = controller.tileSheet.get_imageCustomScale(112, 115, 22, 60,self.width,self.height)
                else:
                    self.image = game.transform.flip(controller.tileSheet.get_imageCustomScale(112, 115, 22, 60,self.width,self.height), True, False)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
        
        self.image.set_colorkey((0,0,0))

class listOfStructures:
    def __init__(self,controller,mapNum):
        self.dir = path.dirname(__file__)
        txtDir = path.join(self.dir,'maps')
        self.text = []
        self.mapNumber = mapNum
        with open(path.join(txtDir,"map"+str(self.mapNumber)+".txt"), 'r') as f:
            for line in f:
                self.text.append(line)
        self.arr = []
        for i in self.text: 
            self.x = i.split("\n")
            self.arr.append(self.x[0])

        self.structures = game.sprite.Group()
        self.fillers = game.sprite.Group()
        self.controller = controller

    def createPlatforms(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                if self.arr[i][j] == "f":
                    structureObj = structure(50,26,25+j*50,13+i*100,"floor",self.controller,None,self.mapNumber)
                    structureObj2 = structure(50,75,25+j*50,61+i*100,"filler",self.controller,None,self.mapNumber)
                    self.structures.add(structureObj)
                    self.fillers.add(structureObj2)
                elif self.arr[i][j] == "w" or self.arr[i][j] == "a":
                    if self.arr[i][j] == "w":
                        structureObj = structure(50,100,25+j*50,50+i*100,"wall",self.controller,"right",self.mapNumber)
                        self.structures.add(structureObj)
                    else:
                        structureObj = structure(50,100,25+j*50,50+i*100,"wall",self.controller,"left",self.mapNumber)
                        self.structures.add(structureObj)
                elif self.arr[i][j] == "p":
                    structureObj = structure(50,20,25+j*50,10+i*100,"platform",self.controller,None,self.mapNumber)
                    self.structures.add(structureObj)
                elif self.arr[i][j] == "c":
                    structureObj = structure(50,100,25+j*50,50+i*100,"ceiling",self.controller,None,self.mapNumber)
                    self.structures.add(structureObj)
                elif self.arr[i][j] == "r":
                    structureObj = structure(50,100,25+j*50,50+i*100,"filler",self.controller,None,self.mapNumber)
                    self.fillers.add(structureObj)
