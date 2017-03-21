from character import *

class Player(Character):
    def attack(self, enemies):
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
        
