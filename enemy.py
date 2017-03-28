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

        self.attack_player()

    def hit(self):
        print "OWWWW I got hit"

    def attack_player(self):
        # Test to see if we overlap with the player.
        player = self._game.get_player()
        can_attack = player.get_rect().colliderect(self.get_rect())
        if can_attack:
            player.hit()
        
        
        
