### Behaviour ###


class Behaviour(object):

    # Each behaviour has a unique id
    GUID = 0

    def __init__(self):
        self.guid = Behaviour.GUID
        Behaviour.GUID += 1

        self.interval = 1

    def apply(self, p, dt, index):
        # Store some data in each particle.
        pass