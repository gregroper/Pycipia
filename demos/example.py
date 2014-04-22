from PyQt4 import QtCore, QtGui
from behaviour.Attraction import Attraction
from behaviour.Collision import Collision
from engine import Particle
from engine.Physics import Physics
from engine.integrator.Verlet import Verlet
from random import randint, random, choice
from lwmath.Vector import Vector


class Example(QtGui.QMainWindow):

    COLOURS = ['red', 'green', 'black', 'blue', 'yellow', 'orange']


    def __init__(self):
        """ Create a physics instance which uses the Verlet integration method"""
        self.physics = Physics()
        self.physics.integrator = Verlet()

        # Design some behaviours for particles
        self.avoidMouse = Attraction()
        self.pullToCenter = Attraction()

        # Allow particle collisions to make things interesting
        self.collision = Collision()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.draw)
        self.timer.start(200)

        super(Example, self).__init__()

    def setup(self):
        for i in range(20):
            # Create a particle
            particle = Particle.Particle(random())
            position = Vector(randint(0, self.width()), randint(0, self.height()))
            particle.setRadius(particle.mass * 10)
            particle.moveTo(position)
            particle.colour = QtGui.QColor(choice(self.COLOURS))

            # Make it collidable
            self.collision.pool.append(particle)

            # Apply behaviours
            particle.behaviours.extend([self.avoidMouse, self.pullToCenter, self.collision])

            # Add to the simulation
            self.physics.particles.append(particle)

        self.pullToCenter.target.x = self.width() / 2.
        self.pullToCenter.target.y = self.height() / 2.
        self.pullToCenter.strength = 120

        self.avoidMouse.setRadius(60)
        self.avoidMouse.strength = -1000

    def draw(self):
        # Step the simulation
        self.physics.step()
        self.repaint()

    def paintEvent(self, event):
        paint = QtGui.QPainter()
        paint.begin(self)

        paint.setRenderHint(QtGui.QPainter.Antialiasing)

        # Clear background
        paint.setBrush(QtCore.Qt.white)
        paint.drawRect(QtCore.QRect())

        # Render particles
        for particle in self.physics.particles:
            #particle = self.physics.particles[i]
            center = QtCore.QPoint(particle.pos._x, particle.pos._y)
            paint.setBrush(particle.colour)
            paint.drawEllipse(center, particle.radius, particle.radius)

        paint.end()

    def mousemove(self):
        self.avoidMouse.target.x = random()  # example.mouse.x
        self.avoidMouse.target.y = random()  # example.mouse.y

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    example = Example()
    example.setup()
    example.show()
    example.raise_()
    sys.exit(app.exec_())