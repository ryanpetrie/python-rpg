import pygame

class TimedEvent(object):
    _last_event_ticks = 0

    def __init__(self, time):
        self.time = time

    def is_active(self):
        ticks = pygame.time.get_ticks()
        elapsed_ticks = ticks - self._last_event_ticks
        return elapsed_ticks < self.time

    def trigger(self):
        self._last_event_ticks = pygame.time.get_ticks()
