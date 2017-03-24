import pygame
from character import *

class Player(Character):

    attack_delay = 500
    _last_attack_time = 0
    
    def attack(self, enemies):
        # Has enough time passed since the last attack?
        time = pygame.time.get_ticks()
        elapsed_time = time - self._last_attack_time
        if elapsed_time < self.attack_delay:
            # Not enough time has passed.
            return
        
        # Compute the rect for the attack.
        attack_rect = self.get_rect()
        offsetx, offsety = FACING_DIRECTIONS[self.get_facing()]
        offsetx *= attack_rect.width
        offsety *= attack_rect.height
        attack_rect.move_ip(offsetx, offsety)

        # Test to see if enemies are hit.
        for enemy in enemies:
            enemy_rect = enemy.get_rect()
            if enemy_rect.colliderect(attack_rect):
                enemy.hit()

        # Update our last attack time.
        self._last_attack_time = time
        
