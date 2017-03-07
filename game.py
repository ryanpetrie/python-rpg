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
        self._screen = pygame.display.set_mode((self._width*2, self._height*2))
        self._canvas = pygame.Surface((self._width, self._height), 0, self._screen)
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
        self._canvas.fill((255, 255, 255))
        self._map.draw(self._canvas)
        self._character.draw(self._canvas, self._map)
        self._enemy.draw(self._canvas, self._map)
        pygame.transform.scale2x(self._canvas, self._screen)
        pygame.display.flip()

    def _handle_input(self):
        speed = self._character.speed
        facing = FACING_DOWN
        rect = self._character.get_rect()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            facing = FACING_LEFT
            rect.x -= speed
        if keys[pygame.K_RIGHT]:
            facing = FACING_RIGHT
            rect.x += speed
        if keys[pygame.K_UP]:
            facing = FACING_UP
            rect.y -= speed
        if keys[pygame.K_DOWN]:
            facing = FACING_DOWN
            rect.y += speed
        if not self._map.collides(rect):
            self._character.set_position(rect.x, rect.y)
            self._character.set_facing(facing)
            self._map.set_center(rect.centerx, rect.centery)

    def _shutdown(self):
        pygame.display.quit()

game = Game()
game.run()
