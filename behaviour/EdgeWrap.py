### Edge Wrap Behaviour ###
from Behaviour import Behaviour
from lwmath.Vector import Vector


class EdgeWrap(Behaviour):

    def __init__(self):
        self.min = Vector()
        self.max = Vector()

        super(EdgeWrap).__init__(self)

    def apply(self, p, dt, index):
        #super p, dt, index
        if p.pos._x + p.radius < self.min._x:
            p.pos._x = self.max._x + p.radius
            p.old_pos._x = p.pos.x
        elif p.pos._x - p.radius > self.max._x:
            p.pos._x = self.min._x - p.radius
            p.old_pos._x = p.pos._x
        if p.pos._y + p.radius < self.min._y:
            p.pos._y = self.max._y + p.radius
            p.old_pos._y = p.pos._y
        elif p.pos._y - p.radius > self.max._y:
            p.pos._y = self.min._y - p.radius
            p.old_pos._y = p.pos._y