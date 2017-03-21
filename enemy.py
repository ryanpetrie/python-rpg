from character import *
from random import randint

class Enemy(Character):
    _steps_left = 0
    _direction = -1
    
    def update(self, time):
        Character.update(self, time)
        if self._steps_left <= 0:
            self._steps_left = randint(10, 30)
            #self._direction = randint(0, 3)
            self._direction = (self._direction + 1) % 4
            
        # Let's move our enemy!!
        x, y = self.get_position()
        if self._direction == 0:
            y += 1
        elif self._direction == 1:
            x += 1
        elif self._direction == 2:
            y -= 1
        else:
            x -= 1
        self.set_position(x, y)
        self._steps_left -= 1

    def hit(self):
        print "OWWWW I got hit"
