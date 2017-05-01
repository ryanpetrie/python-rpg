#! /usr/bin/env python
import pygame
from tilemap import *
from character import *
from enemy import *
from player import *
from gui import *

class Game(object):
    _width = 320
    _height = 240
    TIMER_EVENT = pygame.USEREVENT + 1
    TARGET_FPS = 30

    def __init__(self):
        pygame.init()
        self.enemies = []
        self._screen = pygame.display.set_mode((self._width*2, self._height*2))
        self._canvas = pygame.Surface((self._width, self._height), 0, self._screen)
        self._map = TileMap('test.tmx', self._width, self._height, self)
        self._player = Player('character.tmx', self)
        self._clock = pygame.time.Clock()
        self._gui = Gooey('gui.tmx')

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
        self._gui.text_box(self._canvas,
                           pygame.Rect(0, 0, 128, 48),
                           ["Hello world!","This is a test.","This is ONLY a test."],
                           color=(255, 200, 200),
                           size=16)  # THIS IS ONLY A TEST
        pygame.transform.scale2x(self._canvas, self._screen)
        pygame.display.flip()

    def _handle_input(self):
        speed = self._player.speed
        x, y = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed
        if keys[pygame.K_SPACE]:
            self._player.attack(self.enemies)
        if self._player.move(self._map, x, y):
            rect = self._player.get_rect()
            self._map.set_center(rect.centerx, rect.centery)

    def _shutdown(self):
        pygame.display.quit()
	
    def get_player(self):
        return self._player

    def get_tilemap(self):
        return self._map
		
game = Game()
game.run()
