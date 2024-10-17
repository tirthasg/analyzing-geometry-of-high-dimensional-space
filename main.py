import numpy as np


def get_fraction_outside():
    npoints = 100000
    ndim = 2

    rng = np.random.default_rng(seed=42)
    points = rng.random(size=(npoints, ndim))
    

if __name__ == "__main__":
    get_fraction_outside()