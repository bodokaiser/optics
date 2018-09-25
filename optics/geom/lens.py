import mpmath as mp

from optics.geom.propagation import Propagation
from optics.geom.refraction import Spherical


class Thin:
  """
  Thin lens transfer matrix.
  """

  def __init__(self, focal_length):
    self._focal_length = focal_length

  def abcd(self):
    f = self._focal_length

    T = mp.eye(2)
    T[1, 0] = -1 / f

    return T


class Thick:
  """
  Thick lens transfer matrix.
  """

  def __init__(self, radius1, radius2, thickness):
    self._radius1 = radius1
    self._radius2 = radius2
    self._thickness = thickness

  def abcd(self):
    T1 = Spherical(self._radius1)
    T2 = Propagation(self._thickness)
    T3 = Spherical(self._radius2)

    return T3 * T2 * T1
