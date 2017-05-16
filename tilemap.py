import pytmx, pygame
from pytmx.util_pygame import load_pygame
from spawner import *
from popup_trigger import *

class TileMap(object):
    def __init__(self, filename, screenwidth, screenheight, game):
        # Load the tile data from the file.
        self._map = load_pygame(filename)

        # Get the tile map width and height.
        self._tilex, self._tiley = (self._map.tilewidth, self._map.tileheight)

        # Create rects for the world and the screen.
        self._world_rect = pygame.Rect(0, 0, self._map.width * self._tilex, self._map.height * self._tiley)
        self._screen_rect = pygame.Rect(0, 0, screenwidth, screenheight)

        self._objects = []
        self._create_special_objects(game)

    def _create_special_objects(self, game):
        # Loop through every visible tile to see if we should create something.
        for layer_number in self._map.visible_tile_layers:
            # Get the layer object so we can use its properties.
            layer = self._map.layers[layer_number]
            for y in xrange(layer.height):
                for x in xrange(layer.width):
                    # Get the tile properties
                    props = self._map.get_tile_properties(x, y, layer_number)
                    if props and 'Spawner' in props:
                        rect = pygame.Rect(x * self._tilex, y * self._tiley, self._tilex, self._tiley)
                        spawner = Spawner(rect, game)
                        self._objects.append(spawner)
        # Loop through object layers.
        for layer in self._map.layers:
            if type(layer) != pytmx.TiledObjectGroup:
                continue
            for obj in layer:
                if "trigger_type" in obj.properties:
                    trigger_type = obj.properties["trigger_type"]
                    if trigger_type == "popup":
                        trigger = PopupTrigger(obj, game)
                        self._objects.append(trigger)
                    else:
                        print "Unknown trigger type"


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
            if type(layer) != pytmx.TiledTileLayer:
                continue
            for x, y, image in layer.tiles():
                left = x * self._tilex - self._screen_rect.x
                top = y * self._tiley - self._screen_rect.y
                myrect = pygame.Rect(left, top, self._tilex, self._tiley)
                screen.blit(image, myrect)

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
                for layer in self._map.visible_tile_layers:
                    # Does this tile have collision?
                    props = self._map.get_tile_properties(x, y, layer)
                    if props and "collision" in props and props["collision"]:
                        return True

        # If no collision was found, the rect does not collide.
        return False

    def update(self, time):
        for obj in self._objects:
            obj.update(time)
