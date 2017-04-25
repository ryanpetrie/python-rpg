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

        # Create a font cache.
        self._font_cache = {}
        


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
                    
    def text_box(self, surface, rect, text_list, **kwargs):
        # Handle the keyword arguments.
        if not kwargs: kwargs = {}
        color = kwargs.get('color', (255, 255, 255))
        size = kwargs.get('size', 25)
        
        # Draw the box first.
        self.draw_box(surface, rect)
        # Shrink the rendering rect for the border.
        rect = rect.inflate(-self.BORDER_SIZE, -self.BORDER_SIZE)
        # Get the text to render.
        font = self.get_font(size)
        for text in text_list:
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect() # noob
            # Make sure the text fits.
            if rect.width < text_rect.width:
                text_rect.width = rect.width
            if rect.height < text_rect.height:
                text_rect.height = rect.height
            text_surface = text_surface.subsurface(text_rect)
            # Render the text.
            surface.blit(text_surface, rect)
            # Shrink the rect for the next line.
            rect.height -= font.get_linesize()
            rect.y += font.get_linesize()
        
    def get_font(self, size):
        if size in self._font_cache:
            return self._font_cache[size]
        # Font was not in the cache. Make a new one.
        font = pygame.font.SysFont(None, size)
        self._font_cache[size] = font
        return font
                        
        
