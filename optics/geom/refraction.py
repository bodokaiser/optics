import mpmath as mp


class Planar:
  """
  Planar refraction transfer matrix.
  """

  def __init__(self, n1, n2):
    self._n1 = n1
    self._n2 = n2

  def abcd(self):
    n1 = self._n1
    n2 = self._n2

    T = mp.eye(2)
    T[1, 1] = n1 / n2

    return T


class Spherical(Planar):
  """
  Spherical refraction transfer matrix.
  """

  def __init__(self, n1, n2, radius):
    self.super().__init__(n1, n2)
    self._radius = radius

  def __call__(self, n1, n2, r):
    n1 = self._n1
    n2 = self._n2
    r = self._radius

    T = super(Spherical, self).__call__(n1, n2)
    T[1, 0] = (n1 - n2) / (n2 * r)

    return T
