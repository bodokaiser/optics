import mpmath as mp


def U(u, v, n):
  """
  Two-variables Lommel function "U" of order "n".
  """
  def seq(s): return (-1)**s * (u / v)**(n + 2 * s) * mp.besselj(n + 2 * s, v)

  return mp.nsum(seq, [0, mp.inf])


def V(u, v, n):
  """
  Two-variables Lommel function "V" of order "n".
  """
  def seq(s): return (-1)**s * (u / v)**(-n - 2 * s) * \
      mp.besselj(-n - 2 * s, v)

  return mp.nsum(seq, [0, mp.inf])
