# Optics

This repository contains implementations of common optics methods, for
instance, Gaussian beams and geometrical transfer matrices.

Furtheremore it provides a numerical implementation of

1. [Y. Li and F.T.S. Yu, Intensity distribution near the focus of an apertured focused Gaussian beam][1]
2. [H. Urey, Spot size, depth-of-focus, and diffraction ring intensity formulas for truncated Gaussian beams][2]

that can be used to estimate the aperture limited focus resolution. This
project is not meant to be a standalone library!

## Usage

Install requirements, e.g. using `pip`:

```shell
$ pip install -r requirements.txt
```

See the example notebooks in the repository for specific usage or consult the
source code.

[1]: https://www.sciencedirect.com/science/article/abs/pii/0030401889901971
[2]: https://www.osapublishing.org/ao/abstract.cfm?uri=ao-43-3-620
