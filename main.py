import pygame as game
import characters, sys
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

        self. master = game.display.set_mode((self.width,self.height))
        self.character = characters.character(self.width, self.height)

    def tick(self):
        self.clock.tick(self.frameRate)

    def handleEvents(self):    
        for event in game.event.get():
            if event.type == game.QUIT:
                controller.running = False
            if event.type == game.KEYDOWN:
                #right
                if event.key == game.K_d:
                    self.character.movingRight = True
                #left
                if event.key == game.K_a:
                    self.character.movingLeft = True
                #jump
                if event.key == game.K_SPACE:
                    self.character.jump()

            if event.type == game.KEYUP:
                #right
                if event.key == game.K_d:
                    self.character.movingRight = False
                #left
                if event.key == game.K_a:
                    self.character.movingLeft = False
    def draw(self):
        self.character.draw(self.master)

controller = controller()
while controller.running:
    controller.handleEvents()

    controller.master.fill((0,0,0))
    controller.draw()
    
    game.display.update()
    controller.tick()

game.quit()