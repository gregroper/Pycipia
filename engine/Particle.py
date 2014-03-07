# Particle
from lwmath.Vector import Vector


class Particle(object):
    GUID = 0

    def __init__(self, mass=1.0):
        self.mass = mass

        # Set a unique id.
        self.id = 'p' + str(Particle.GUID)
        Particle.GUID += 1

        # Set initial mass.
        self.setMass(self.mass)

        # Set initial radius.
        self.setRadius(1.0)

        # Apply forces.
        self.fixed = False

        # Behaviours to be applied.
        self.behaviours = []

        # Current position.
        self.pos = Vector()

        # Current velocity.
        self.vel = Vector()

        # Current force.
        self.acc = Vector()

        # Previous state.
        self.old_pos = Vector()
        self.old_vel = Vector()
        self.old_acc = Vector()

    def moveTo(self, pos):
        """Moves the particle to a given location vector."""
        self.pos.copy(pos)
        self.old_pos.copy(pos)

    def setMass(self, mass=1.0):
        """ Sets the mass of the particle. """
        self.mass = mass
        # The inverse mass.
        self.massInv = 1.0 / self.mass

    def setRadius(self, radius=1.0):
        """ Sets the radius of the particle. """
        self.radius = radius
        self.radiusSq = self.radius**2

    def update(self, dt, index):
        """ Applies all behaviours to derive new force. """
        if not self.fixed:
            for behaviour in self.behaviours:
                behaviour.apply(self, dt, index)
