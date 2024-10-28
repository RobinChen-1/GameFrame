from GameFrame import RoomObject
import random

class Opponent(RoomObject):

    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        self.side = random.choice(["left", "right"])
        if self.side == "left":
            self.x = 0 
            self.x_speed = 10
            image = self.load_image("Opponent_left.png")
        else:
            self.x = 800  
            self.x_speed = -10
            image = self.load_image("Opponent_right.png")
        
        