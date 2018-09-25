import mpmath as mp


class Base:
  """
  Base class for intensity distribution for a Gaussian beam propagating a
  circular aperture.
  """

  def __init__(self, radius, focal_length, gaussian):
    """
    Initializes intensity distribution for aperture limited lens with aperture
    and Gaussian beam instance.
    """
    self._radius = radius
    self._gaussian = gaussian
    self._focal_length = focal_length

  @property
  def radius(self):
    """
    Returns the aperture radius.
    """
    return self._radius

  @property
  def waist(self):
    """
    Returns the beam waist of the Gaussian beam at the center of the
    aperture.
    """
    return self._gaussian.waist()

  @property
  def wavenumber(self):
    """
    Returns the wavenumber of the Gaussian beam propagating through the
    circular aperutre.
    """
    return self._gaussian.wavenumber

  @property
  def wavelength(self):
    """
    Returns the wavelength of the Gaussian beam propagating through the
    circular aperutre.
    """
    return self._gaussian.wavelength

  @property
  def focal_length(self):
    """
    Returns the focal length, the distance between the aperture and the
    focus spot of the Gaussian beam.
    """
    return self._focal_length

  def __call__(self, r, z):
    raise NotImplementedError()


class Urey(Base):
  """
  Radial intensity distribution in the focal plane for a converging Gaussian
  beam propagating through a circular according to [H. Urey, 2004][1].

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

    def fn(u): return u * mp.exp(-(u / T)**2) * mp.besselj(0, mp.pi * u * rn)

    return mp.abs(mp.quad(fn, [0, 1]))**2 / T**2

  def normalized_radius(self, r):
    """
    Returns the normalized radius in the focus plane.
    """
    return r / (self.wavelength * self.focal_ratio)
