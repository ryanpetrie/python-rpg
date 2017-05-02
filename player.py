import pygame
from character import *
from animator import *
from timed_event import *

WEAPON_LAYER = 1

class Player(Character):

    _attack_event = TimedEvent(500)
    _attack_rect = pygame.Rect(0, 0, 0, 0)
    speed = 4

    def draw(self, screen, tilemap):
        Character.draw(self, screen, tilemap)
        if self.is_in_attack():
            offsetx, offsety = tilemap.get_offset()
            rect = self._attack_rect.move(-offsetx, -offsety)
            sprite = get_animated_tile_image(self._sprites, self.get_facing(), 0, WEAPON_LAYER, self._update_time)
            #self._sprites.get_tile_image(self.get_facing(), 0, WEAPON_LAYER)
            screen.blit(sprite, rect)

    def is_in_attack(self):
        return self._attack_event.is_active()
        
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
        self._attack_event.trigger()

        # Reset attack animation.
        props = self._sprites.get_tile_properties(self.get_facing(), 0, WEAPON_LAYER)
        reset_animation(props)

    def hit(self):
        if self.is_invul():
            return
        print "I'm the player don't hit me"
        self.go_invul()        

    def move(self, tilemap, rel_x, rel_y):
        if self.is_in_attack():
            return False
        return Character.move(self, tilemap, rel_x, rel_y)

    def handle_input(self, keys):
        x, y = 0, 0
        tilemap = self._game.get_tilemap()
        if keys[pygame.K_LEFT]:
            x -= self.speed
        if keys[pygame.K_RIGHT]:
            x += self.speed
        if keys[pygame.K_UP]:
            y -= self.speed
        if keys[pygame.K_DOWN]:
            y += self.speed
        if keys[pygame.K_SPACE]:
            self.attack(self._game.enemies)
        if self.move(tilemap, x, y):
            rect = self.get_rect()
            tilemap.set_center(rect.centerx, rect.centery)
        
        
