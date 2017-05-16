import pygame
from gui import *

class Popup(object):
    def __init__(self, game):
        self._game = game
        self._gui = game.get_gui()  # so messy
        game.input_stack.append(self)
        game.paused_count += 1
        game.drawables.append(self)

    def handle_input(self, keys, released):
        if released[pygame.K_SPACE]:
            self._game.input_stack.pop()
            self._game.paused_count -= 1
            self._game.drawables.remove(self)

    def draw(self, canvas):
        self._gui.draw_box(canvas, pygame.Rect(0, 0, 32, 32))
