### Spring ###
import lwmath.Vector


class Spring(object):

    def __init__(self, p1, p2, rest_length=100, stiffness=1.0):
        self.p1 = p1
        self.p2 = p2
        self.rest_length = rest_length
        self.stiffness = stiffness
        self._delta = lwmath.Vector.Vector()

    def apply(self):
        """F = -kx"""
        self._delta.copy(self.p2.pos).sub(self.p1.pos)

        dist = self._delta.mag() + 0.000001
        force = (dist - self.rest_length) / (dist * (self.p1.massInv + self.p2.massInv)) * self.stiffness

        if not self.p1.fixed:
            self.p1.pos.add(self._delta.clone().scale(force * self.p1.massInv))

        if not self.p2.fixed:
            self.p2.pos.add(self._delta.scale(-force * self.p2.massInv))