import pytmx, pygame
from pytmx.util_pygame import load_pygame
from animator import *

class Character(object):
    def __init__(self, filename):
        # Load the character's sprites from the tile map.
        self._sprites = load_pygame(filename)

        # Start the character at (0,0).
        self._rect = pygame.Rect(0, 0, self._sprites.tilewidth, self._sprites.tileheight)

    def update(self, time):
        animate_tilemap(self._sprites, time)
        
    def draw(self, screen, tilemap):
        # Get the first sprite from the tilemap.
        surface = self._sprites.get_tile_image(0, 0, 0)

        # Offset the rect by the map's offset.
        xoffset, yoffset = tilemap.get_offset()
        myrect = self._rect.move(-xoffset, -yoffset)

        # Draw it.
        screen.blit(surface, myrect)

    def get_position(self):
        # Return the (x,y) position of the character.
        return self._rect.topleft

    def set_position(self, x, y):
        # Set the character's top-left corner.
        self._rect.x = x
        self._rect.y = y
