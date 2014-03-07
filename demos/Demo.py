""" Demo """
import random
from engine.Particle import Particle
from engine.Physics import Physics


class Demo(object):

    COLOURS = ['DC0048', 'F14646', '4AE6A9', '7CFF3F', '4EC9D9', 'E4272E']

    def __init__(self, width, height):

        self.physics = Physics()
        self.mouse = Particle()
        self.mouse.fixed = True
        self.height = height
        self.width = width

        self.renderTime = 0
        self.counter = 0

    def setup(self, full=True):
        """ Override and add paticles / springs here """
        raise NotImplementedError('Override')

    def init(self, container, renderer):
        """ Initialise the demo (override). """
        # Build the scene.
        self.setup(renderer)

        # Give the particles random colours.
        for particle in self.physics.particles:
            if not particle.colour:
                particle.colour = random.choice(Demo.COLOURS)

    def step(self):
        """ Update loop. """
        self.physics.step()
        self.renderer.render(self.physics)

	""" Clean up after yourself. """
	def destroy(self):

		# console.log self., 'destroy'

		# Remove event handlers.
		document.removeEventListener 'touchmove', self.mousemove, false
		document.removeEventListener 'mousemove', self.mousemove, false
		document.removeEventListener 'resize', self.resize, false

		# Remove the render output from the DOM.
		try container.removeChild self.renderer.domElement
		catch error

		do self.renderer.destroy
		do self.physics.destroy

		self.renderer = null
		self.physics = null
		self.mouse = null

	def mousemove(self, event):
        """ Handler for window mousemove event. """
		event.preventDefault()

		if event.touches and !!event.touches.length
			touch = event.touches[0]
			self.mouse.pos.set touch.pageX, touch.pageY
		else
			self.mouse.pos.set event.clientX, event.clientY
