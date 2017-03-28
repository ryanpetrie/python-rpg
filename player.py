import pygame
from character import *

WEAPON_LAYER = 1

class Player(Character):

    attack_delay = 500
    _last_attack_time = 0
    _attack_rect = pygame.Rect(0, 0, 0, 0)

    def draw(self, screen, tilemap):
        Character.draw(self, screen, tilemap)
        if self.is_in_attack():
            offsetx, offsety = tilemap.get_offset()
            rect = self._attack_rect.move(-offsetx, -offsety)
            sprite = self._sprites.get_tile_image(self.get_facing(), 0, WEAPON_LAYER)
            screen.blit(sprite, rect)

    def is_in_attack(self):
        time = pygame.time.get_ticks()
        elapsed_time = time - self._last_attack_time
        return elapsed_time < self.attack_delay
        
    def attack(self, enemies):
        # Has enough time passed since the last attack?
        if self.is_in_attack():
            return
        
        # Compute the rect for the attack.
        self._attack_rect = self.get_rect()
        offsetx, offsety = FACING_DIRECTIONS[self.get_facing()]
        offsetx *= self._attack_rect.width
        offsety *= self._attack_rect.height
        self._attack_rect.move_ip(offsetx, offsety)

        # Test to see if enemies are hit.
        for enemy in enemies:
            enemy_rect = enemy.get_rect()
            if enemy_rect.colliderect(self._attack_rect):
                enemy.hit()

        # Update our last attack time.
        self._last_attack_time = pygame.time.get_ticks()

    def hit(self):
        print "I'm the player don't hit me"

    def move(self, tilemap, rel_x, rel_y):
        if self.is_in_attack():
            return False
        return Character.move(self, tilemap, rel_x, rel_y)
