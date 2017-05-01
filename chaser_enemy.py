from enemy import *
import pygame
from pygame.math import Vector2

class ChaserEnemy(Enemy):
    attack_distance = 128
    speed = 64  # pixels per second
    collides = False
    
    def update(self, time):
        Enemy.update(self, time)
        player = self._game.get_player()

        # Get the vector to the player.
        player_pos = Vector2(player.get_position())
        enemy_pos = Vector2(self.get_position())
        enemy_to_player = player_pos - enemy_pos

        # See if we're close enough to chase.
        length = enemy_to_player.length()
        if length <= self.attack_distance and length > 0.1:
            # Turn our time into seconds.
            time = time / 1000.0
            # Determine how far we're stepping.
            distance = self.speed * time
            # Move us toward the player.
            enemy_to_player.scale_to_length(distance)
            if self.collides:
                self.move(self._game.get_tilemap(),
                          int(round(enemy_to_player.x)),
                          int(round(enemy_to_player.y)))
            else:
                enemy_pos += enemy_to_player
                self.set_position(int(round(enemy_pos.x)),
                                  int(round(enemy_pos.y)))


                
            
