from GameFrame import Level
from Objects.Title import Title, Subtitle 

class WelcomeScreen(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image
        self.set_background_image("Background.png")

        # add title object
        self.add_room_object(Title(self, 240, 200))
        self.add_room_object(Subtitle(self, 325, 550))