#! /usr/bin/env python
import pygame
from tilemap import *
from character import *
from enemy import *

class Game(object):
    _width = 320
    _height = 240
    TIMER_EVENT = pygame.USEREVENT + 1
    TARGET_FPS = 30

    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((self._width,self._height))
        self._map = TileMap('test.tmx', self._width, self._height)
        self._character = Character('character.tmx')
        self._enemy = Enemy('character.tmx')
        self._clock = pygame.time.Clock()

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
        frame_time = self._clock.tick()
        self._handle_input()

        # Update stuff.
        self._character.update(frame_time)
        self._enemy.update(frame_time)

        # Draw the screen.
        self._screen.fill((255, 255, 255))
        self._map.draw(self._screen)
        self._character.draw(self._screen, self._map)
        self._enemy.draw(self._screen, self._map)
        pygame.display.flip()

    def _handle_input(self):
        xpos, ypos = self._character.get_position()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            xpos -= 1
        if keys[pygame.K_RIGHT]:
            xpos += 1
        if keys[pygame.K_UP]:
            ypos -= 1
        if keys[pygame.K_DOWN]:
            ypos += 1
        rect = pygame.Rect(xpos, ypos, 16, 16)
        if not self._map.collides(rect):
            self._character.set_position(xpos, ypos)

    def _shutdown(self):
        pygame.display.quit()

game = Game()
game.run()
