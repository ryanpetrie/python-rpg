#! /usr/bin/env python
import pygame
from tilemap import *

class Game(object):
    _width = 320
    _height = 240
    TIMER_EVENT = pygame.USEREVENT + 1
    TARGET_FPS = 30

    offset_test = 0
    
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((self._width,self._height))
        self._map = TileMap('test.tmx', self._width, self._height)

    def run(self):
        pygame.time.set_timer(self.TIMER_EVENT, 1000 / self.TARGET_FPS)
        while True:
            ok = self._process_events()
            if not ok:
                break
        self._shutdown()

    def _process_events(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return False
        elif event.type == self.TIMER_EVENT:
            self._run_frame()
        return True

    def _run_frame(self):
        self._screen.fill((255, 255, 255))
        self._map.set_offset(0, self.offset_test)
        self._map.draw(self._screen)
        pygame.display.flip()
        self.offset_test += 1

    def _shutdown(self):
        pygame.display.quit()

game = Game()
game.run()
