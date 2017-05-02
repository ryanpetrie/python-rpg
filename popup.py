import pygame
from gui import *

class Popup(object):
    def __init__(self, game, gui):
        self._game = game
        self._gui = gui
        game.input_stack.append(self)
        game.paused = True
        game.drawables.append(self)

    def handle_input(self, keys):
        if keys[pygame.K_SPACE]:
            self._game.input_stack.pop()
            self._game.paused = False
            self._game.drawables.remove(self)

    def draw(self, canvas):
        self._gui.draw_box(canvas, pygame.Rect(0, 0, 32, 32))