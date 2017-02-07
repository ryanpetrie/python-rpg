import pytmx, pygame
from pytmx.util_pygame import load_pygame

class TileMap(object):
    def __init__(self, filename, screenwidth, screenheight):
        self._map = load_pygame(filename)
        self._tilex, self._tiley = (self._map.tilewidth, self._map.tileheight)
        self._world_rect = pygame.Rect(0, 0, self._map.width * self._tilex, self._map.height * self._tiley)
        self._screen_rect = pygame.Rect(0, 0, screenwidth, screenheight)
        self._font = pygame.font.SysFont(None, 25)

    def get_offset(self):
        return self._screen_rect.topleft

    def set_offset(self, x, y):
        self._screen_rect.x = x
        self._screen_rect.y = y
        self._screen_rect.clamp_ip(self._world_rect)

    def draw(self, screen):
        for layer in self._map.layers:
            for x, y, image in layer.tiles():
                left = x * self._tilex - self._screen_rect.x
                top = y * self._tiley - self._screen_rect.y
                myrect = pygame.Rect(left, top, self._tilex, self._tiley)
                screen.blit(image, myrect)
        xoffset, yoffset = self.get_offset()
        message = "Offset: " + str(xoffset) + ", " + str(yoffset)
        surface = self._font.render(message, True, (15, 0, 255))
        myrect = pygame.Rect(0, 0, surface.get_width(), surface.get_height())
        screen.blit(surface, myrect)

