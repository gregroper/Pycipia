### Edge Bounce Behaviour ###
from Behaviour import Behaviour
from lwmath.Vector import Vector


class EdgeBounce(Behaviour):

    def __init__(self):
        self.min = Vector()
        self.max = Vector()

        super(EdgeBounce).__init__(self)

    def apply(self, p, dt, index):

        if p.pos.x - p.radius < self.min._x:
            p.pos.x = self.min._x + p.radius
        elif p.pos.x + p.radius > self.max._x:
            p.pos.x = self.max._x - p.radius

        if p.pos.y - p.radius < self.min._y:
            p.pos.y = self.min._y + p.radius
        elif p.pos.y + p.radius > self.max._y:
            p.pos.y = self.max._y - p.radius
