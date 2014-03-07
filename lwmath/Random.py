# Random 
import random


class Random(object):

    @staticmethod
    def random(min_val=0, max_val=1):
        return min_val + random.random() * (max_val - min_val)

    @staticmethod
    def int(min_val, max_val):
        return random.randint(min_val, max_val)

    @staticmethod
    def sign(prob=0.5):
        return 1 if random.random() < prob else -1

    @staticmethod 
    def bool(prob=0.5):
        return random.random() < prob

    @staticmethod
    def item(items):
        return random.choice(items)