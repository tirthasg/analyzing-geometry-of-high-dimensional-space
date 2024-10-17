import numpy as np


def get_fraction_outside(npoints: int, ndim: int):
    rng = np.random.default_rng(seed=42)
    points = rng.random(size=(npoints, ndim))

    squared_distance_from_origin = np.sum(np.square(points), axis=1)
    mask = squared_distance_from_origin > 1
    points_outside = points[mask]

    fraction_of_points_outside = points_outside.shape[0] / npoints
    return fraction_of_points_outside


if __name__ == "__main__":
    print(get_fraction_outside(npoints=100000, ndim=2))
