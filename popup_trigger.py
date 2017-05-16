from trigger import *
from popup import *

class PopupTrigger(Trigger):
    def __init__(self, obj, game):
        Trigger.__init__(self, obj, game)

    def _on_player_collide(self):
        popup = Popup(self._game)
