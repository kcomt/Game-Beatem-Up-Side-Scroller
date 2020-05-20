import pygame as game
import characters, sys,structures

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
        self.character = characters.character(self.width, self.height)
        self.structure1 = structures.structure(200,20,600,400,"platform")
        self.structure2 = structures.structure(20,300,1000,self.height-300/2,"platform")
        self.structure3 = structures.structure(1200,20,600,790,"floor")

        self.all_sprites = game.sprite.Group()
        self.platforms = game.sprite.Group()
        self.all_sprites.add(self.character)
        self.platforms.add(self.structure1)
        self.platforms.add(self.structure2)
        self.platforms.add(self.structure3)

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
        self.all_sprites.draw(self.master)
        self.platforms.draw(self.master)
        
    def tick(self):
        self.clock.tick(self.frameRate)

    def update(self):
        self.all_sprites.update()
        self.character.rect.y += 1
        hits = game.sprite.spritecollide(self.character,self.platforms,False)
        self.character.rect.y -= 1
        if hits:
            if self.character.rect.bottom  < hits[0].rect.bottom and hits[0].typeOf != "floor":
                self.character.rect.y = hits[0].rect.top - self.character.height
                self.character.somethingUnderTrue()

            elif hits[0].typeOf == "floor":
                self.character.rect.y = hits[0].rect.top - self.character.height
                self.character.somethingUnderTrue()
        else:
            if self.character.rect.y > 600 and self.character.rect.y < 1000:
                print(self.structure3.rect.bottom)
            self.character.notSomethingUnder()

controller = controller()

while controller.running:
    controller.tick()
    controller.handleEvents()
    #update
    controller.update()
    #render/erase
    controller.master.fill((0,0,0))
    #draw
    controller.draw()
    
    game.display.flip()


game.quit()