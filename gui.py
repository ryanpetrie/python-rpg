import pygame
import pytmx
from pytmx.util_pygame import load_pygame

class Gooey(object):

    def __init__(self, filename):
        # Load the GUI tiles.
        self._tiles = load_pygame(filename)

        # Remember the tile width and height.
        self._tilex = self._tiles.tilewidth
        self._tiley = self._tiles.tileheight

        # Set up GUI surfaces.
        self._topleft = self._tiles.get_tile_image(0, 0, 0)
        self._top = self._tiles.get_tile_image(1, 0, 0)
        self._topright = self._tiles.get_tile_image(2, 0, 0)
        self._left = self._tiles.get_tile_image(0, 1, 0)
        self._middle = self._tiles.get_tile_image(1, 1, 0)
        self._right = self._tiles.get_tile_image(2, 1, 0)
        self._bottomleft = self._tiles.get_tile_image(0, 2, 0)
        self._bottom = self._tiles.get_tile_image(1, 2, 0)
        self._bottomright = self._tiles.get_tile_image(2, 2, 0)


    def draw_box(self, surface, rect):
        # Make sure rect is a multiple of tile sizes.
        width = (rect.width + self._tilex - 1) / self._tilex
        height = (rect.height + self._tiley - 1) / self._tiley

        # Make sure we are at least 2x2 tiles.
        if width < 2:
            width = 2
        if height < 2:
            height = 2
        
        # Draw the box.
        # +--------+
        # |########|
        # +--------+
        for y in xrange(height):
            for x in xrange(width):
                tile_rect = pygame.Rect(rect.x + x * self._tilex, rect.y + y * self._tiley, self._tilex, self._tiley)
                if x == 0:
                    # Handle left edge.
                    if y == 0:
                        surface.blit(self._topleft, tile_rect)
                    elif y == height - 1:
                        surface.blit(self._bottomleft, tile_rect)
                    else:
                        surface.blit(self._left, tile_rect)
                elif x == width - 1:
                    # Handle right edge.
                    if y == 0:
                        surface.blit(self._topright, tile_rect)
                    elif y == height - 1:
                        surface.blit(self._bottomright, tile_rect)
                    else:
                        surface.blit(self._right, tile_rect)
                else:
                    # Handle middle column.
                    if y == 0:
                        surface.blit(self._top, tile_rect)
                    elif y == height - 1:
                        surface.blit(self._bottom, tile_rect)
                    else:
                        surface.blit(self._middle, tile_rect)
                    
                    
                    
                        
        
