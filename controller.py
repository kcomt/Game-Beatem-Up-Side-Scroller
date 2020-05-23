import pygame as game
import characters,structures
from os import path
from characters import *

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
        self.height = 800
        self.master = game.display.set_mode((self.width,self.height))
        self.load()
        self.character = characters.character(self.width, self.height,self)
        self.structure1 = structures.structure(200,20,600,500,"platform")
        self.structure2 = structures.structure(20,600,1000,self.height-600/2,"wall")
        self.structure3 = structures.structure(1200,20,600,790,"floor")

        self.all_sprites = game.sprite.Group()
        self.platforms = game.sprite.Group()
        self.all_sprites.add(self.character)
        self.platforms.add(self.structure1)
        self.platforms.add(self.structure2)
        self.platforms.add(self.structure3)

        #keyPressed
        self.dPressed = False
        self.aPressed = False
        self.spacePressed = False
        
    def handleEvents(self):
        self.move()
        for event in game.event.get():
            if event.type == game.QUIT:
                self.running = False

    def draw(self):
        self.all_sprites.draw(self.master)
        self.platforms.draw(self.master)
        
    def tick(self):
        self.clock.tick(self.frameRate)
        self.character.tick()
        if self.character.frameLag > 0:
            self.character.frameLag -= 1
        
    def update(self):
        self.all_sprites.update()

    def move(self):
        keys=game.key.get_pressed()
        if keys[game.K_d]:
            self.character.moveH("right")
        if keys[game.K_a]:
            self.character.moveH("left")
        if keys[game.K_SPACE]:
            self.character.jump()
        
        if keys[game.K_SPACE] and keys[game.K_d]:
            self.character.wallJumpRight(self.master)
        
        if keys[game.K_SPACE] and keys[game.K_a]:
            self.character.wallJumpLeft(self.master)

    def load(self):
        # load high score
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir,'sprites')
        # load spritesheet image
        self.spritesheet = Spritesheet(path.join(img_dir,"2.png"))