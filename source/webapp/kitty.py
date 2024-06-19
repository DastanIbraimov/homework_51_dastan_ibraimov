from random import randint


class Kitty:
    IMAGES = {
        'sad': 'images/sad.png',
        'good': 'images/good.png',
        'bua': 'images/bua.jpeg',
        'sleep': 'images/sleep.png',
        'wakeup': 'images/wakeup.jpg',
    }

    def __init__(self):
        self.name = ''
        self.age = 1
        self.fullness = 40
        self.mood = 40
        self.is_sleeping = False
        self.image = self.IMAGES['good']

    def play(self):
        if self.is_sleeping:
            self.is_sleeping = False
            self.mood -= 5
            self.set_image('wakeup')
        else:
            self.fullness -= 10
            chance = randint(1, 3)
            if chance == 1:
                self.mood = 0
            else:
                self.mood += 15

            if 30 <= self.mood < 100:
                self.set_image('good')
            if self.mood < 30:
                self.set_image('sad')

    def feed(self):
        if not self.is_sleeping:
            self.fullness += 15
            self.mood += 5
            if self.fullness >= 100:
                self.set_image('bua')
            elif 30 <= self.mood < 100:
                self.set_image('good')

    def sleep(self):
        self.is_sleeping = True
        self.set_image('sleep')

    def set_image(self, image_name):
        self.image = self.IMAGES[image_name]

    def validate_params(self):
        if self.fullness > 100:
            self.fullness = 100
            self.mood -= 35
        elif self.fullness < 0:
            self.fullness = 0

        if self.mood > 100:
            self.mood = 100
        elif self.mood < 0:
            self.mood = 0
