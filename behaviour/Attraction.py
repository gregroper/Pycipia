### Attraction Behaviour ###
from Behaviour import Behaviour
from lwmath.Vector import Vector


class Attraction(Behaviour):

    def __init__(self, radius=1000, strength=100.0):
        self.target = Vector()
        self.radius = radius
        self.strength = strength

        self._delta = Vector()
        self.setRadius(self.radius)

        super(Attraction, self).__init__()

    def setRadius(self, radius):
        """ Sets the effective radius of the behaviours. """
        self.radius = radius
        self.radiusSq = radius**2
    
    def apply(self, p, dt, index):
        # Vector pointing from particle to target.
        self._delta.copy(self.target).sub(p.pos)

        # Squared distance to target.
        distSq = self._delta.mag_squared()

        # Limit force to behaviour radius.
        if 0.000001 < distSq < self.radiusSq:
            # Calculate force vector.
            self._delta.norm().scale(1.0 - distSq / self.radiusSq)
            #Apply force.
            p.acc.add(self._delta.scale(self.strength))
