import numpy as np
import mpmath as mp

from math import lommel


def to_u(a, f, k, z):
  """
  Converts axial distance from focal spot to generalized coordinate "u".

  The axial distance from the geometrical focal spot is defined in the
  direction of beam propagation.

  Args:
    a: aperture radius
    f: focal length
    k: wavenumber
    z: axial distance
  """
  return (a / f)**2 * k * z


def to_v(a, f, k, r):
  """
  Converts radial distance from focal spot to generalized coordinate "v".

  The radial distance from the geometrical focal spot is defined with respect
  to the focal plane perpendicular to the beam propagation axis.
  """
  return (a / f) * k * r


def intensity(r, z, w):
  u = to_u(z)
  v = to_v(r)

  α = (a / w)**2
  β = v**2 / (u**2 + 4 * α**2)

  I = 2 * α**2 * mp.exp(-α) / (mp.cosh(α) - 1) / (u**2 + 4 * α**2)

  if mp.sqrt(u**2 + 4 * α**2) < v:
    U1 = lommel.U(u, v, 1)
    U2 = lommel.U(u, v, 2)

    return I * ((mp.im(U1) + mp.re(U2))**2 + (mp.re(U1) - mp.im(U2))**2)

  if mp.sqrt(u**2 + 4 * α**2) > v:
    V0 = lommel.V(u, v, 0)
    V1 = lommel.V(u, v, 1)

    return I * ((mp.im(V0) - mp.re(V1) - mp.exp(α * (1 - β)) * mp.cos(u * (1 + β) / 2))**2 + (mp.re(V0) + mp.im(V1))**2 + mp.exp(α * (1 - β)) * mp.sin(u * (1 + β) / 2))

  return 0
