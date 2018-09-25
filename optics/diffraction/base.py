import mpmath as mp


class Diffraction:
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
  def gaussian(self):
    """
    Returns the Gaussian beam instance.
    """
    return self._gaussian

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
