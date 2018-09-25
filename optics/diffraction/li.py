import mpmath as mp

from optics.math import lommelU, lommelV
from optics.diffraction.base import Diffraction as BaseDiffraction


class Diffraction(BaseDiffraction):
  """
  Intensity distribution near the focal spot for a Gaussian beam propagating
  through a aperture limited lens according to [Y. Li, 1989][1].

  [1]: https://www.sciencedirect.com/science/article/abs/pii/0030401889901971
  """

  def alpha(self):
    """
    Returns the alpha (truncation) parameter.
    """
    return (self._radius / self._gaussian.waist())**2

  def beta(self, u, v):
    """
    Returns the beta parameter.
    """
    return v**2 / (u**2 + 4 * self.alpha()**2)

  def __call__(self, r, z=1e-10):
    """
    Returns the intensity distribution near the focal spot.
    """
    u = self.normalized_distance(z)
    v = self.normalized_radius(r)

    α = self.alpha()
    β = self.beta(u, v)

    I = 2 * α**2 * mp.exp(-α) / (mp.cosh(α) - 1) / (u**2 + 4 * α**2)

    if mp.sqrt(u**2 + 4 * α**2) < v:
      U1 = lommelU(u, v, 1)
      U2 = lommelU(u, v, 2)

      U1s = mp.re(U1)
      U1c = mp.im(U1)
      U2s = mp.re(U2)
      U2c = mp.im(U2)

      return I * ((U1c + U2s)**2 + (U1s - U2c)**2)

    if mp.sqrt(u**2 + 4 * α**2) > v:
      V0 = lommelV(u, v, 0)
      V1 = lommelV(u, v, 1)

      V0s = mp.re(V0)
      V0c = mp.im(V0)
      V1s = mp.re(V1)
      V1c = mp.im(V1)

      exp = mp.exp(α * (1 - β))
      cos = mp.cos(u * (1 + β) / 2)
      sin = mp.sin(u * (1 + β) / 2)

      return I * ((V0c - V1s - exp * cos)**2 + (V0s + V1c + exp * sin)**2)

    raise ValueError('invalid coordinates')

  def normalized_radius(self, r):
    """
    Returns the normalized radial distance from focal spot "v".
    """
    return (self.radius / self.focal_length) * self.wavenumber * r

  def normalized_distance(self, z):
    """
    Returns the normalized axial distance from focal spot "u".
    """
    return (self.radius / self.focal_length)**2 * self.wavenumber * z
