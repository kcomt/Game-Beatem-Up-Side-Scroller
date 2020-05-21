import pygame as game
import characters,structures

class controller:
    def __init__(self):
        game.init()
        #(delay,interval), the delay is the number of milliseconds before the first repeated pygame.KEYDOWN will be sent
        game.key.set_repeat(75,75)
        self.clock = game.time.Clock()
        self.running = True
        self.frameRate = 60
        self.width = 1200
        self.height = 800
        self.master = game.display.set_mode((self.width,self.height))
        self.character = characters.character(self.width, self.height,self)
        self.structure1 = structures.structure(200,20,600,400,"platform")
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
        for event in game.event.get():
            if event.type == game.QUIT:
                self.running = False
            if event.type == game.KEYDOWN:
                self.character.movingLeft = False
                self.character.movingRight = False
                #right
                if event.key == game.K_d:
                    self.character.movingRight = True 
                    self.dPressed = True
                #left
                if event.key == game.K_a:
                    self.character.movingLeft = True
                #jump
                if event.key == game.K_SPACE:
                    self.character.jump()
                    self.spacePressed = True

            if self.dPressed and self.spacePressed:
                self.character.wallJump()

            if event.type == game.KEYUP:
                #right
                if event.key == game.K_d:
                    self.character.movingRight = False
                    self.dPressed = False

                #left
                if event.key == game.K_a:
                    self.character.movingLeft = False
                    self.aPressed = False
            
            self.spacePressed = False

    def draw(self):
        self.all_sprites.draw(self.master)
        self.platforms.draw(self.master)
        
    def tick(self):
        self.clock.tick(self.frameRate)
        
    def update(self):
        self.all_sprites.update()
