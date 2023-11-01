from pico2d import load_image
import random

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

import game_world
import game_framework

class Bird:
    image = None
    def __init__(self):
        self.x = random.randint(100, 1500)
        self.y = random.randint(300, 550)
        self.frame = random.randint(0, 4)
        self.action = random.randint(0,2)
        self.face_dir = 1
        self.dir = 1
        if self.image == None:
            self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.action = (self.action + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) // 5
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if int(self.frame) == 4 and int(self.action) == 0:
            self.frame = 0
            self.action = 2
        if self.x >= 1600:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1
        pass

    def handle_event(self, event):
        pass

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 182, int(self.action) * 168, 182, 168,
                                           0, '', self.x, self.y, 100, 100)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 182, int(self.action) * 168, 182, 168,
                                           0, 'h', self.x, self.y, 100, 100)
        pass