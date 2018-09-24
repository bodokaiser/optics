import unittest

from numpy import testing as npt

from optics.beam import GaussianBeam
from optics.geom import Propagation, ThinLens


class TestGaussian(unittest.TestCase):

  def setUp(self):
    self.gaussian = GaussianBeam(waist=1e-6, wavelength=532e-9)

  def test_propagation(self):
    T = Propagation(10e-2).abcd()

    gaussian = self.gaussian.propagate(T)

    self.assertEqual(gaussian.origin, 10e-2)
    self.assertEqual(gaussian.rayleigh, self.gaussian.rayleigh)

  def test_thin_lens(self):
    T = ThinLens(25e-3).abcd()

    gaussian = self.gaussian.propagate(T)

    npt.assert_almost_equal(gaussian.origin, 0)
    self.assertEqual(1 / gaussian.curvature(), 1 /
                     self.gaussian.curvature() - 1 / 25e-3)