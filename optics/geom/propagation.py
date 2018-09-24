import numpy as np


class Propagation:
  """
  Propagation transfer matrix.
  """

  def __init__(self, distance):
    self._distance = distance

  def abcd(self):
    d = self._distance

    T = np.identity(2)
    T[0, 1] = d

    return T
