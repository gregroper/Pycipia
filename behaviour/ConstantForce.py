### Constant Force Behaviour ###
from Behaviour import Behaviour
from lwmath.Vector import Vector


class ConstantForce(Behaviour):

    def __init__(self):
        self.force = Vector()
        super(ConstantForce).__init__(self)

    def apply(self, p, dt,index):
        p.acc.add(self.force)