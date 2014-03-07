### Physics Engine ###
import time
from integrator.Euler import Euler


class Physics(object):

    def __init__(self, integrator=Euler()):
        self.integrator = integrator

        # Fixed timestep.
        self.timestep = 1.0 / 60

        # Friction within the system.
        self.viscosity = 0.005

        # Global behaviours.
        self.behaviours = []

        # Time in seconds.
        self._time = 0.0

        # Last step duration.
        self._step = 0.0

        # Current time.
        self._clock = None

        # Time buffer.
        self._buffer = 0.0

        # Max iterations per step.
        self._maxSteps = 4

        # Particles in system.
        self.particles = []

        # Springs in system.
        self.springs = []

    def integrate(self, dt):
        """Performs a numerical integration step."""

        # Drag is inversely proportional to viscosity.
        drag = 1.0 - self.viscosity

        # Update particles / apply behaviours.
        for index, particle in enumerate(self.particles):
            for behaviour in self.behaviours:
                behaviour.apply(particle, dt, index)
            particle.update(dt, index)

        # Integrate motion.
        self.integrator.integrate(self.particles, dt, drag)

        # Compute all springs.
        for spring in self.springs:
            spring.apply()

    # Steps the system. ###
    def step(self):
        # Initialise the clock on first step.
        if self._clock is None:
            self._clock = time.time()

        # Compute delta time since last step.
        current_time = time.time()
        delta = current_time - self._clock

        # No sufficient change.
        if delta <= 0.0:
            return

        # Update the clock.
        self._clock = current_time

        # Increment time buffer.
        self._buffer += delta

        # Integrate until the buffer is empty or until the
        # maximum amount of iterations per step is reached.
        step = 0
        while self._buffer >= self.timestep and step < self._maxSteps:

            # Integrate motion by fixed timestep.
            self.integrate(self.timestep)

            # Reduce buffer by one timestep.
            self._buffer -= self.timestep

            # Increment running time.
            self._time += self.timestep

            step += 1

        # Store step time for debugging.
        self._step = time.time() - current_time