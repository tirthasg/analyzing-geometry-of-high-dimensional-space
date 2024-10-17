import numpy as np


def get_fraction_outside(npoints: int, ndim: int) -> float:
    """
    Computes the fraction of point outside of an unit sphere, which is contained within an unit cube in n-dimensional space

    Args:
        npoints (int): Number of points to generate in n-dimensional space
        ndim (int): Number of dimensions

    Returns:
        fraction_of_points_outside (float): Fraction of points outside of unit sphere in n-dimensional space
    """
    rng = np.random.default_rng(seed=42)
    points = rng.random(size=(npoints, ndim))

    squared_distance_from_origin = np.sum(np.square(points), axis=1)
    mask = squared_distance_from_origin > 1
    points_outside = points[mask]

    fraction_of_points_outside = points_outside.shape[0] / npoints
    return fraction_of_points_outside


if __name__ == "__main__":
    npoints = 100000
    for ndim in range(2, 21):
        fraction_of_points_outside = get_fraction_outside(npoints=npoints, ndim=ndim)
        print(f"For {ndim}, fraction outside = {fraction_of_points_outside}")
