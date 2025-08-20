from GameFrame import RoomObject
import math
import pygame
        
class Opponent(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.health = 50
        
        image = self.load_image("Opponent_Right.png")
        self.set_image(image,222,224)
        self.x_speed = -5

    def step(self):
        if self.x < self.room.character.x + 60:
            self.x_speed = 0
        else:
            self.x_speed = -5

    


    
