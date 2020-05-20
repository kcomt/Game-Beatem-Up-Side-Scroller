import pygame as game
import controller
game.init()
controller = controller.controller()

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