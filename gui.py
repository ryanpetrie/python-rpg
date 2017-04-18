import pygame
import pytmx
from pytmx.util_pygame import load_pygame

class Gooey(object):

    BORDER_SIZE = 5

    def __init__(self, filename):
        # Load the GUI tiles.
        self._tiles = load_pygame(filename)

        # Remember the tile width and height.
        self._tilex = self._tiles.tilewidth
        self._tiley = self._tiles.tileheight

        # Create a font.
        self._font = pygame.font.SysFont(None, 25)


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
                # Assume we're in the middle of the box.
                xedge = 1
                yedge = 1
                if x == 0:
                    # Handle left edge.
                    xedge = 0
                elif x == width - 1:
                    # Handle right edge.
                    xedge = 2
                if y == 0:
                    # Handle top edge.
                    yedge = 0
                elif y == height - 1:
                    # Handle bottom edge.
                    yedge = 2
                tile = self._tiles.get_tile_image(xedge, yedge, 0)
                surface.blit(tile, tile_rect)
                    
    def text_box(self, surface, rect, text, color = (255, 255, 255)):
        self.draw_box(surface, rect)
        text_surface = self._font.render(text, True, color)
        rect = rect.inflate(-self.BORDER_SIZE, -self.BORDER_SIZE)
        surface.blit(text_surface, rect)
        
                    
                        
        
