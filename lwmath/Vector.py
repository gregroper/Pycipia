# 2D Vector
import math


class Vector(object):

    @staticmethod
    def add(v1, v2):
        """Adds two vectors and returns the product. """
        return Vector(v1._x + v2._x, v1._y + v2._y)

    @staticmethod
    def sub(v1, v2):
        """Subtracts v2 from v1 and returns the product."""
        return Vector(v1._x - v2._x, v1._y - v2._y)

    @staticmethod
    def project(v1, v2):
        """Projects one vector (v1) onto another (v2)"""
        return v1.clone().scale(v1.dot(v2) / v1.mag_squared())

    def __init__(self, x=0.0, y=0.0):
        """Creates a new Vector instance."""
        self._x, self._y = x, y

    def set(self, x, y):
        """Sets the components of this vector."""
        self._x, self._y = x, y
        return self

    def add(self, v):
        """Add a vector to this one."""
        self._x += v._x
        self._y += v._y
        return self

    def sub(self, v):
        """Subtracts a vector from this one."""
        self._x -= v._x
        self._y -= v._y
        return self

    def scale(self, f):
        """Scales this vector by a value."""
        self._x *= f
        self._y *= f
        return self

    def dot(self, v):
        """Computes the dot product between vectors."""
        return self._x * v._x + self._y * v._y

    def cross(self, v):
        """# Computes the cross product between vectors."""
        return (self._x * v._y) - (self._y * v._x)

    def mag(self):
        """Computes the magnitude (length)."""
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def mag_squared(self):
        """Computes the squared magnitude (length)."""
        return self._x ** 2 + self._y ** 2

    def dist(self, v):
        """Computes the distance to another vector."""
        dx = v._x - self._x
        dy = v._y - self._y
        return math.sqrt(dx * dx + dy * dy)

    def dist_squared(self, v):
        """# Computes the squared distance to another vector."""
        dx = v._x - self._x
        dy = v._y - self._y
        return dx * dx + dy * dy

    def norm(self):
        """# Normalises the vector, making it a unit vector (of length 1)."""
        m = math.sqrt(self._x ** 2 + self._y ** 2)
        self._x /= m
        self._y /= m
        return self

    def limit(self, limit):
        """# Limits the vector length to a given amount."""
        m_sq = self._x ** 2 + self._y ** 2
        if m_sq > limit**2:
            m = math.sqrt(m_sq)
            self._x /= m
            self._y /= m
            self._x *= limit
            self._y *= limit

    def copy(self, v):
        """# Copies components from another vector."""
        self._x = v._x
        self._y = v._y
        return self

    def clone(self):
        """# Clones this vector to a new identical one."""
        return Vector(self._x, self._y)

    def clear(self):
        """# Resets the vector to zero."""
        self._x = 0.0
        self._y = 0.0
