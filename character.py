import pytmx, pygame
from pytmx.util_pygame import load_pygame
from animator import *

FACING_DOWN = 0
FACING_RIGHT = 1
FACING_UP = 2
FACING_LEFT = 3

FACING_DIRECTIONS = [(0, +1), (+1, 0), (0, -1), (-1, 0)]


class Character(object):
    _facing = 0
    speed = 4
    
    def __init__(self, filename, game):
        # Load the character's sprites from the tile map.
        self._sprites = load_pygame(filename)

        # Start the character at (0,0).
        self._rect = pygame.Rect(0, 0, self._sprites.tilewidth, self._sprites.tileheight)

        # Save the game object.
        self._game = game

    def update(self, time):
        animate_tilemap(self._sprites, time)
        
    def draw(self, screen, tilemap):
        # Get the animated surface.
        surface = get_animated_tile_image(self._sprites, self._facing, 0, 0)

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

    def get_rect(self): # NOOB
        return self._rect.copy()

    def set_facing(self, direction):
        self._facing = direction

    def get_facing(self):
        return self._facing

    def move(self, tilemap, rel_x, rel_y):
        new_rect = self._rect.move(rel_x, rel_y)
        if tilemap.collides(new_rect):
            return False
        # If we get here, there are no collisions. 
        self._rect = new_rect
        if rel_x < 0:
            self._facing = FACING_LEFT
        if rel_x > 0:
            self._facing = FACING_RIGHT
        if rel_y < 0:
            self._facing = FACING_UP
        if rel_y > 0:
            self._facing = FACING_DOWN
        return True
            
        

