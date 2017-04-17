from timed_event import *
from wander_enemy import *

class Spawner(object):

    def __init__(self, rect, game):
        self._rect = rect
        self._game = game
        self._spawn_timer = TimedEvent(10 * 1000)

    def update(self, time):
        if not self._spawn_timer.is_active():
            self._spawn()

    def _spawn(self):
        # Trigger the timed event.
        self._spawn_timer.trigger()

        # Create the new enemy.
        new_enemy = WanderEnemy('character.tmx', self._game)
        new_enemy.set_position(self._rect.center[0], self._rect.center[1])

        # Add it to the enemy list.
        self._game.enemies.append(new_enemy)

