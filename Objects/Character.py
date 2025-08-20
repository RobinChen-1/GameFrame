from GameFrame import RoomObject, Globals
from Objects.Opponent import Opponent
from GameFrame.Level import Level
import pygame

class Character(RoomObject):

    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.stand = self.load_image("Stand.png")
        self.punching = self.load_image("Punch.png")
        self.kicking = self.load_image("Kick.png")
        self.defending = self.load_image("Defense.png")
        self.set_image(self.stand, 130, 180)
        self.attack_range = 60
        self.damage = 25
        
        self.is_punching = False
        self.is_kicking = False
        self.is_defending = False
        self.handle_key_events = True

    def key_pressed(self, key):
        if key[pygame.K_a]:
            self.x -= 10
        elif key[pygame.K_d]:
            self.x += 10
        
        if key[pygame.K_k]:
            self.punch()
            self.set_image(self.punching, 130, 180)
        elif key[pygame.K_l]:
            self.kick()
            self.set_image(self.kicking, 130, 180)
        elif key[pygame.K_o]:
            self.defend()
            self.set_image(self.defending, 130, 180)
        else:
            self.set_image(self.stand, 130, 180)

    def keep_in_room(self):
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.width

    def step(self):
        self.keep_in_room()

    def punch(self):
        self.is_punching = True
        self.check_punch_hit()
        attack_x_start = self.x + 10 
        attack_x_end = attack_x_start + self.attack_range
        for obj in self.room.objects:
            if hasattr(obj, 'take_damage'): 
                if self.is_in_attack_range(obj, attack_x_start, attack_x_end):
                    obj.take_damage(self.damage)
    
    def kick(self):
        self.is_kicking = True

    def defend(self):
        self.is_defending = True

    def check_punch_hit(self):
        opponent = self.room.opponent 
        if opponent is not None: 
            punch_range = pygame.Rect(self.x + 50, self.y, 30, 30)
            opponent_rect = pygame.Rect(opponent.x, opponent.y, opponent.width, opponent.height)


    def is_in_attack_range(self, opponent, start_x, end_x):
        return start_x <= opponent.x <= end_x

