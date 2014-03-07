### Wander Behaviour ###
from Behaviour import Behaviour
import math
import random


class Wander(Behaviour):

    def __init__(self, jitter=0.5, radius=100, strength=1.0):
        self.jitter = jitter
        self.radius = radius
        self.strength = strength
        self.theta = random.random() * math.pi * 2

        super(Wander).__init__(self)

    def apply(self, p, dt, index):
        self.theta += (random.random() - 0.5) * self.jitter * math.pi * 2

        p.acc.x += math.cos(self.theta) * self.radius * self.strength
        p.acc.y += math.sin(self.theta) * self.radius * self.strength

