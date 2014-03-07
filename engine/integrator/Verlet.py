# Velocity Verlet Integrator
from Integrator import Integrator
from lwmath.Vector import Vector


class Verlet(Integrator):
    
    # v = x - ox
    # x = x + (v + a * dt * dt)

    def integrate(self, particles, dt, drag):

        pos = Vector()

        dtSq = dt * dt

        for p in particles:
            if not p.fixed:

                # Scale force to mass.
                p.acc.scale(p.massInv)

                # Derive velocity.
                p.vel.copy(p.pos).sub(p.old_pos)

                # Apply friction.
                if drag:
                    p.vel.scale(drag)

                # Apply forces to new position.
                pos.copy(p.pos).add(p.vel.add(p.acc.scale(dtSq)))

                # Store old position.
                p.old_pos.copy(p.pos)

                # update position.
                p.pos.copy(pos)

                # Reset forces.
                p.acc.clear()

