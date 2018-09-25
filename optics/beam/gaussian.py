import mpmath as mp


class Gaussian:
  """
  Gaussian represents a Gaussian beam from optics.
  """

  def __init__(self, waist, wavelength, amplitude=1, origin=0):
    """
    Initializes a Gaussian with given wavelength and beam waist.
    """
    self._origin = origin
    self._waist = waist
    self._wavelength = wavelength
    self._amplitude = amplitude

  def fwhm(self, z=0):
    """
    Returns the Full Width at Half Maximum at z.
    """
    z += self.origin

    return mp.sqrt(2 * mp.log(2)) * self.waist(z)

  def waist(self, z=0):
    """
    Returns the beam waist at z.
    """
    if z == 0:
      return self._waist

    return self._waist * mp.sqrt(1 + (z / self.rayleigh)**2)

  def curvature(self, z=0):
    """
    Returns the radius of curvature at z.
    """
    z += self.origin

    if z == 0:
      return mp.inf

    return z * (1 + (self.rayleigh / z)**2)

  def intensity(self, r, z):
    """
    Returns the (relative) intensity at (r,z).
    """
    z += self.origin

    return (self.waist(0) / self.waist(z))**2 * \
        mp.exp(-2 * r**2 / self.waist(z)**2)

  def propagate(self, T):
    """
    Returns new Gaussian beam with updated parameters from transfer matrix.
    """
    z = self.origin
    k = self.wavenumber
    q = self.parameter
    q = (T[0, 0] * q + T[0, 1]) / (T[1, 0] * q + T[1, 1])

    z = mp.re(q) + z
    w = mp.sqrt(2 * mp.im(q) / k)

    return Gaussian(waist=w, origin=z, wavelength=self.wavelength)

  @property
  def origin(self):
    """
    Returns the axial origin.
    """
    return self._origin

  @property
  def parameter(self):
    """
    Returns the complex beam parameter.
    """
    return self.origin + 1j * self.rayleigh

  @property
  def rayleigh(self):
    """
    Returns the rayleigh length of the beam.
    """
    return self.wavenumber * self.waist()**2 / 2

  @property
  def wavenumber(self):
    """
    Returns the wavenumber of the beam.
    """
    return 2 * mp.pi / self.wavelength

  @property
  def wavelength(self):
    """
    Returns the wavelength of the beam.
    """
    return self._wavelength
