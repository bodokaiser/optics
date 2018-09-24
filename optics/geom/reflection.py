import numpy as np


class Planar:
  """
  Planar reflection transfer matrix.
  """

  def abcd(self):
    return np.identity(2)


class Spherical(Planar):
  """
  Spherical reflection transfer matrix.
  """

  def __init__(self, radius):
    self._radius = radius

  def abcd(self, r):
    r = self._radius

    T = super(Spherical, self)
    T[1, 0] = 2 / r

    return T
