from character import *
from random import randint

class Enemy(Character):
    _steps_left = 0
    _direction = -1

	def update(self, time):
		Character.update(self, time)

    def hit(self):
        print "OWWWW I got hit"

    def attack_player(self):
        # Test to see if we overlap with the player.
        player = self._game.get_player()
        can_attack = player.get_rect().colliderect(self.get_rect())
        if can_attack:
            player.hit()
        
        
        
