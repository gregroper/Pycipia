### Collision Behaviour ###
from Behaviour import Behaviour
import math
from lwmath.Vector import Vector
# TODO: Collision response for non Verlet integrators.


class Collision(Behaviour):

    def __init__(self, useMass=True, callback=None):
        self.useMass = useMass
        self.callback = callback
        # Pool of collidable particles.
        self.pool = []
        # Delta between particle positions.
        self._delta = Vector()
        super(Collision, self).__init__()

    def apply(self, p, dt, index):
        # Check pool for collisions.
        for o in self.pool[index:]:
            if o is not p:                
                # Delta between particles positions.
                self._delta.copy(o.pos).sub(p.pos)

                # Squared distance between particles.
                distSq = self._delta.mag_squared()

                # Sum of both radii.
                radii = p.radius + o.radius

                # Check if particles collide.
                if distSq <= radii**2:

                    # Compute real distance.
                    dist = math.sqrt(distSq)

                    # Determine overlap.
                    overlap = radii - dist
                    overlap += 0.5

                    # Total mass.
                    mt = p.mass + o.mass

                    # Distribute collision responses.
                    r1 = o.mass / mt if self.useMass else 0.5
                    r2 = p.mass / mt if self.useMass else 0.5

                    # Move particles so they no longer overlap.
                    p.pos.add(self._delta.clone().norm().scale(overlap * -r1))
                    o.pos.add(self._delta.norm().scale(overlap * r2))

                    # Fire callback if defined.
                    if self.callback is not None:
                        self.callback(p, o, overlap)