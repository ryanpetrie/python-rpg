import pytmx, pygame
from pytmx.util_pygame import load_pygame

class TileMap(object):
    def __init__(self, filename, screenwidth, screenheight):
        # Load the tile data from the file.
        self._map = load_pygame(filename)

        # Get the tile map width and height.
        self._tilex, self._tiley = (self._map.tilewidth, self._map.tileheight)

        # Create rects for the world and the screen.
        self._world_rect = pygame.Rect(0, 0, self._map.width * self._tilex, self._map.height * self._tiley)
        self._screen_rect = pygame.Rect(0, 0, screenwidth, screenheight)

        # Create a test font.
        self._font = pygame.font.SysFont(None, 25)

    def get_offset(self):
        return self._screen_rect.topleft

    def set_offset(self, x, y):
        self._screen_rect.x = x
        self._screen_rect.y = y
        # Clamp the screen rect to the world rect.
        self._screen_rect.clamp_ip(self._world_rect)

    def set_center(self, x, y):
        self._screen_rect.center = (x, y)
        # Clamp the screen rect to the world rect.
        self._screen_rect.clamp_ip(self._world_rect)

    def draw(self, screen):
        # Draw each tile.
        for layer in self._map.layers:
            for x, y, image in layer.tiles():
                left = x * self._tilex - self._screen_rect.x
                top = y * self._tiley - self._screen_rect.y
                myrect = pygame.Rect(left, top, self._tilex, self._tiley)
                screen.blit(image, myrect)
                
        # Draw a test message.
        xoffset, yoffset = self.get_offset()
        message = "Offset: " + str(xoffset) + ", " + str(yoffset)
        surface = self._font.render(message, True, (15, 0, 255))
        myrect = pygame.Rect(0, 0, surface.get_width(), surface.get_height())
        screen.blit(surface, myrect)

    def collides(self, rect):
        if not self._world_rect.contains(rect):
            # rect is outside the world boundaries.
            return True
        
        # Determine the tile bounds of the rect.
        firstx = rect.left / self._tilex
        firsty = rect.top / self._tiley
        lastx = rect.right / self._tilex
        lasty = rect.bottom / self._tiley

        for y in xrange(firsty, lasty + 1):
            for x in xrange(firstx, lastx + 1):
                for layer in xrange(len(self._map.layers)):
                    # Does this tile have collision?
                    props = self._map.get_tile_properties(x, y, layer)
                    if props and "collision" in props and props["collision"]:
                        return True

        # If no collision was found, the rect does not collide.
        return False
