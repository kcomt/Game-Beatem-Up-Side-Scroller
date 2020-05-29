import pygame as game
import characters, structures, inGameGUI
from os import path

class Spritesheet:
    # utility class for loading and parsing spritesheets
    def __init__(self, filename,size):
        self.spritesheet = game.image.load(filename).convert_alpha()
        self.size = size
    def get_image(self, x, y, width, height):
        # grab an image out of a larger spritesheet
        image = game.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = game.transform.scale(image, (width*self.size, height*self.size))
        return image
    def get_imageCustomScale(self, x, y, width, height,outPutWidth,outPutHeight):
        # grab an image out of a larger spritesheet
        image = game.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = game.transform.scale(image, (outPutWidth, outPutHeight))
        return image

class controller:
    def __init__(self):
        game.init()
        game.mixer.init()
        #(delay,interval), the delay is the number of milliseconds before the first repeated pygame.KEYDOWN will be sent
        game.key.set_repeat(75,75)
        self.clock = game.time.Clock()
        self.running = True
        self.frameRate = 60
        self.width = 1200
        self.height = 900
        self.master = game.display.set_mode((self.width,self.height))
        self.load()
        self.character = characters.character(self.width, self.height,self)
        self.structure1 = structures.structure(200,20,600,400,"platform")
        self.structure2 = structures.structure(20,600,1000,self.height-600/2,"wall")
        self.structure3 = structures.structure(1200,20,600,790,"floor")
        self.healthBarImage = inGameGUI.healthBar(self.width,self.height,self)

        self.all_sprites = game.sprite.Group()
        self.platforms = game.sprite.Group()
        self.inGameGUIs = game.sprite.Group()
        self.all_sprites.add(self.character)
        self.platforms.add(self.structure1)
        self.platforms.add(self.structure2)
        self.platforms.add(self.structure3)
        self.inGameGUIs.add(self.healthBarImage)

        self.rightPressed = False
        self.leftPRessed = False
        self.downPressed = False

    def load(self):
        # load high score
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir,'sprites')
        # load spritesheet image
        self.spritesheet = Spritesheet(path.join(img_dir,"2.png"),2)
        self.healthBarImage = Spritesheet(path.join(img_dir,"healthBar.png"),1)

    def handleEvents(self):
        self.move()
        for event in game.event.get():
            if event.type == game.QUIT:
                self.running = False

    def draw(self):
        self.all_sprites.draw(self.master)
        self.platforms.draw(self.master)
        self.inGameGUIs.draw(self.master)

    def tick(self):
        self.clock.tick(self.frameRate)
       
    def update(self):
        self.all_sprites.update()

    def move(self):
        keys=game.key.get_pressed()
        anyKeyPressed = False
        self.character.colliFromHori = False
        #right foward dash
        if keys[game.K_o] and keys[game.K_d]:
            if self.character.somethingUnder:
                self.character.fowardDash("right")
                anyKeyPressed = True
            else:
                self.character.fowardAir("right")
                anyKeyPressed = True
        #left foward dash
        elif keys[game.K_o] and keys[game.K_a]:
            if self.character.somethingUnder:
                self.character.fowardDash("left")
                anyKeyPressed = True
            else:
                self.character.fowardAir("left")
                anyKeyPressed = True
        #down air
        elif keys[game.K_o] and keys[game.K_s]:
            if self.character.somethingUnder:
                self.character.neutralDown()
                anyKeyPressed = True
            else:
                self.character.downAir()
                anyKeyPressed = True
        else:
            #last key pressed should determine if player should go right, left or down
            #right
            if keys[game.K_d]:
                if self.character.currentMove == "crouching":
                    if not self.rightPressed:
                        self.rightPressed = True
                        self.character.moveH("right")
                        anyKeyPressed = True
                else:
                    self.rightPressed = True
                    self.character.moveH("right")
                    anyKeyPressed = True
            else:
                self.rightPressed = False
            #left
            if keys[game.K_a]:
                if self.character.currentMove == "crouching":
                    if not self.leftPressed:
                        self.leftPressed = True
                        self.character.moveH("left")
                        anyKeyPressed = True
                else:
                    self.leftPressed = True
                    self.character.moveH("left")
                    anyKeyPressed = True
            else:
                self.leftPressed = False
            #down
            if keys[game.K_s]:
                if self.character.currentMove == "moving":
                    if not self.downPressed:
                        self.downPressed = True
                        self.character.setSpriteMovement("crouching",self.character.lastDirection)
                        anyKeyPressed = True
                elif self.character.somethingUnder and self.character.animationLagObj.amount == 0:
                    self.downPressed = True
                    self.character.setSpriteMovement("crouching",self.character.lastDirection)
                    anyKeyPressed = True
            else:
                self.downPressed = False
            #up
            if keys[game.K_SPACE]:
                self.character.jump()
                anyKeyPressed = True
            #attack
            if keys[game.K_o]:
                self.character.neutral()
                anyKeyPressed = True
            #right wall jump
            if keys[game.K_SPACE] and keys[game.K_d]:
                self.character.wallJump("right")
                anyKeyPressed = True
            #left wall jump
            if keys[game.K_SPACE] and keys[game.K_a]:
                self.character.wallJump("left")
                anyKeyPressed = True

        if not anyKeyPressed and self.character.somethingUnder and self.character.animationLagObj.amount == 0:
            self.character.setSpriteMovement("standing",self.character.lastDirection)    
