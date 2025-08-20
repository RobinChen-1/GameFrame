from GameFrame import Level, Globals
from Objects.Character import Character
from Objects.Opponent import Opponent
from Objects.Hud import Score, Lives

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        self.set_background_image("Background.png")
        self.character = Character(self,550,500)
        self.add_room_object(self.character)
        self.opponent = Opponent(self,1080,460)
        self.add_room_object(self.opponent)

        self.score = Score(self, 
                           Globals.SCREEN_WIDTH/2 - 20, 20, 
                           str(Globals.SCORE))
        self.add_room_object(self.score)
    

    