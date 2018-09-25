import mpmath as mp

from optics.geometrical import ThinLens, Propagation
from optics.diffraction.base import Diffraction as BaseDiffraction


class Diffraction(BaseDiffraction):
  """
  Radial intensity distribution in the focal plane for a converging Gaussian
  beam propagating through a circular aperture according geometrical optics
  with naive beam clipping.
  """

  def transfer(self):
    """
    Returns the transfer matrix of the optical lens system.
    """
    T1 = ThinLens(self.focal_length).abcd()
    T2 = Propagation(self.focal_length).abcd()

    return T2 * T1

  def __call__(self, r, z=0):
    """
    Returns the intensity distribution near the focal spot.
    """
    if r > self.radius:
      return 0

    T = self.transfer()

    return self.gaussian.propagate(T).intensity(r, z)
