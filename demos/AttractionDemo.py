from Demo import Demo


class AttractionDemo(Demo):

    def setup(self, full=True):

        super(AttractionDemo).__init__(self, full)

        min = Vector(0.0, 0.0)
        max = Vector(self.width, self.height)
        
        bounds = EdgeBounce(min, max)

        self.physics.integrator = Verlet()

        attraction = Attraction(self.mouse.pos, 1200, 1200)
        repulsion = Attraction(self.mouse.pos, 200, -2000)
        collide = Collision()

        max = 400 if full else 200

        for i in range(max):

            p = Particle(Random.random(0.1, 3.0)
            p.setRadius(p.mass * 4)

            p.moveTo(Vector(Random(0, self.width), Random(0, self.height)))

            p.behaviours.append(attraction)
            p.behaviours.append(repulsion)
            p.behaviours.append(bounds)
            p.behaviours.append(collide)

            collide.pool.append(p)

            self.physics.particles.append(p)