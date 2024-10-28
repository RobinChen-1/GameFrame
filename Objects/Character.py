from GameFrame import RoomObject, Globals
from GameFrame.Level import Level
import pygame

class Character(RoomObject):

    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Stand.png")
        self.set_image(image,130,180)

        self.handle_key_events = True

    def key_pressed(self, key):

        if key[pygame.K_a]:
            self.x -= 10
        elif key[pygame.K_d]:
            self.x += 10

    def keep_in_room(self):
        if self.x < 0:
            self.x = 0
        elif self.x + self.width> Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.width

    def step(self):
        self.keep_in_room()