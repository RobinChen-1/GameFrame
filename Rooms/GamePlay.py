from GameFrame import Level
from Objects.Character import Character
from Objects.Opponent import Opponent

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")

        self.add_room_object(Character(self,550,500))
        self.add_room_object(Opponent(self, 0, 500))