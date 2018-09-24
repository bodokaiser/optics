# Aperture focused Gaussian beam

This repository provides the numerical implementation of

1. [Y. Li and F.T.S. Yu, Intensity distribution near the focus of an apertured focused Gaussian beam][1]
2. [H. Urey, Spot size, depth-of-focus, and diffraction ring intensity formulas for truncated Gaussian beams][2]

as well as a coarse approximation using the ray matrix method. The results can
be used to estimate the aperture limited focus resolution.

[1]: https://www.sciencedirect.com/science/article/abs/pii/0030401889901971
[2]: https://www.osapublishing.org/ao/abstract.cfm?uri=ao-43-3-620

## Usage

Install requirements, e.g. using `pip`:

```shell
$ pip install -r requirements.txt
```

Run tests:

```shell
$ python -m unittest discover -s optics -p '*_test.py'
```
