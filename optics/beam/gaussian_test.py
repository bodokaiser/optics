import unittest
import mpmath as mp

from optics.beam import GaussianBeam
from optics.geometrical import Propagation, ThinLens


class TestGaussian(unittest.TestCase):

  def setUp(self):
    self.gaussian = GaussianBeam(waist=1e-6, wavelength=532e-9)

  def est_propagation(self):
    T = Propagation(10e-2).abcd()

    gaussian = self.gaussian.propagate(T)

    self.assertEqual(gaussian.origin, 10e-2)
    self.assertEqual(gaussian.rayleigh, self.gaussian.rayleigh)

  def test_thin_lens(self):
    T = ThinLens(25e-3).abcd()

    gaussian = self.gaussian.propagate(T)

    self.assertAlmostEqual(1 / gaussian.curvature(),
                           1 / self.gaussian.curvature() - 1 / 25e-3)
