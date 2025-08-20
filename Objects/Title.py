from GameFrame import RoomObject
import pygame

class Title(RoomObject):
    """
    The object for displaying the title
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Title.png")
        self.set_image(image,800,350)

class Subtitle(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Subtitle.png")
        self.set_image(image,598,52)

        # register for key events
        self.handle_key_events = True 
        
    def key_pressed(self, key):
        """
        If the key pressed is space the game will start
        """
        
        if key[pygame.K_SPACE]:
            self.room.running = False
