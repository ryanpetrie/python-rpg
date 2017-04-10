from timed_event import *

class Spawner(object):

    def __init__(self, rect, game):
        self._rect = rect
        self._game = game
        self._spawn_timer = TimedEvent(10 * 1000)

    def update(self, time):
        pass
