import mpmath as mp

from optics.diffraction.base import Diffraction as BaseDiffraction


class Diffraction(BaseDiffraction):
  """
  Radial intensity distribution in the focal plane for a converging Gaussian
  beam propagating through a circular aperture according to [H. Urey, 2004][1].

  [1]: https://www.osapublishing.org/ao/abstract.cfm?uri=ao-43-3-620
  """

  @property
  def focal_ratio(self):
    """
    Returns the focal ratio parameter.
    """
    return self.focal_length / (2 * self.radius)

  @property
  def truncation(self):
    """
    Returns the truncation parameter.
    """
    return self.waist / self.radius

  def __call__(self, r):
    """
    Returns the radial intensity distribution at the geometrical focal spot.
    """
    T = self.truncation
    rn = self.normalized_radius(r)

    def integrand(u):
      return u * mp.exp(-(u / T)**2) * mp.besselj(0, mp.pi * u * rn)

    return abs(mp.quad(integrand, [0, 1]))**2 / T**2

  def normalized_radius(self, r):
    """
    Returns the normalized radius in the focus plane.
    """
    return r / (self.wavelength * self.focal_ratio)
