import pygame as game
from os import path

class Camera:
    def __init__(self, width, height):
        self.camera = game.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.lastDirection = "right"
        self.lastx = 0
        self.lastright = 0
        self.dx = 0
    
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        if self.lastDirection != target.lastDirection:
            if target.lastDirection == "left":
                self.dx = target.rect.right-self.lastx
                self.lastDirection = "left"
            else:
                self.lastDirection = "right"
        if target.lastDirection == "right":
            x = -target.rect.x + int(1200 / 2)
            self.lastx = target.rect.x
        else:
            x = -target.rect.right + self.dx + int(1200 / 2)
        y = -target.rect.bottom + 50 + int(900 / 2)
        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - 1200), x)  # right
        y = max(-(self.height - 800), y)  # bottom
        self.camera = game.Rect(x, y, self.width, self.height)