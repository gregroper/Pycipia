### Euler Integrator ###
from Integrator import Integrator
from lwmath.Vector import Vector


class Euler(Integrator):

    # v += a * dt
    # x += v * dt

    def integrate(self, particles, dt, drag):

        vel = Vector()
                
        for p in particles:
            if not p.fixed:
                
                # Store previous location.
                p.old_pos.copy(p.pos)

                # Scale force to mass.
                p.acc.scale(p.massInv)

                # Duplicate velocity to preserve momentum.
                vel.copy(p.vel)

                # Add force to velocity.
                p.vel.add(p.acc.scale(dt))

                # Add velocity to position.
                p.pos.add(vel.scale(dt))

                # Apply friction.
                if drag:
                    p.vel.scale(drag)

                # Reset forces.
                p.acc.clear()