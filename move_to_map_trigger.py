from trigger import *

class MoveToMapTrigger(Trigger):
    def _on_player_collide(self):
        self._game.move_to_map(self._object.properties["map"])
