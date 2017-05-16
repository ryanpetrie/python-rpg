import pygame

class Trigger(object):
    def __init__(self, obj, game):
        self._object = obj
        self._game = game
        self._rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
        self._triggered = False

    def update(self, time):
        if self.collides_with_player():
            if not self._triggered:
                self._triggered = True
                self._on_player_collide()
        else:
            self._triggered = False

    def collides_with_player(self):
        player = self._game.get_player()
        player_rect = player.get_rect()
        return player_rect.colliderect(self._rect)
        
    def _on_player_collide(self):
        pass
