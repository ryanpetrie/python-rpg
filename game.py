#! /usr/bin/env python
import pygame
from tilemap import *
from character import *
from enemy import *
from player import *
from gui import *
from popup import *

class Game(object):
    _width = 320
    _height = 240
    TIMER_EVENT = pygame.USEREVENT + 1
    TARGET_FPS = 30

    def __init__(self):
        pygame.init()
        self.enemies = []
        self.paused = False
        self.drawables = []

        self._screen = pygame.display.set_mode((self._width*2, self._height*2))
        self._canvas = pygame.Surface((self._width, self._height), 0, self._screen)
        self._map = TileMap('test.tmx', self._width, self._height, self)
        self._player = Player('character.tmx', self)
        self._clock = pygame.time.Clock()
        self._gui = Gooey('gui.tmx')

        self.input_stack = [self._player]

    def run(self):
        pygame.time.set_timer(self.TIMER_EVENT, 1000 / self.TARGET_FPS)
        while True:
            ok = self._process_events()
            if not ok:
                break
        self._shutdown()

    def get_player(self):
        return self._player

    def _process_events(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return False
        elif event.type == self.TIMER_EVENT:
            self._run_frame()
        return True

    def _run_frame(self):
        frame_time = self._clock.tick()
        self._handle_input()

        # Update stuff.
        if not self.paused:
            self._map.update(frame_time)
            self._player.update(frame_time)
            for enemy in self.enemies:
                enemy.update(frame_time)

        # Draw the screen.
        self._canvas.fill((255, 255, 255))
        self._map.draw(self._canvas)
        self._player.draw(self._canvas, self._map)
        for enemy in self.enemies:
            enemy.draw(self._canvas, self._map)
        for thingy in self.drawables:
            thingy.draw(self._canvas)
        pygame.transform.scale2x(self._canvas, self._screen)
        pygame.display.flip()

    def _handle_input(self):
        keys = pygame.key.get_pressed()
        top = self.input_stack[-1]
        top.handle_input(keys)
        if keys[pygame.K_p]:
            popup = Popup(self, self._gui)


    def _shutdown(self):
        pygame.display.quit()
	
    def get_tilemap(self):
        return self._map
		
game = Game()
game.run()
