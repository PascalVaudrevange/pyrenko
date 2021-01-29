import itertools
import math
import numpy as np
import pandas as pd


def _process_bin(c: int, cuts: [int], i: int) -> [int]:
    if i == 0:
        result = [c]
    else:
        diff = c - cuts[i-1]
        if abs(diff) == 1:
            result = [c]
        elif abs(diff) > 1:
            # if there is a jump of more than one box size,
            # fill the gaps
            s = np.sign(diff)
            result = range(cuts[i - 1] + s, c + s, s)
        else:
            # ignore duplicates
            result = []
    return result


def get_data(r: float, sigma: float, dt: float = 0.0001, n_timestep: int = 10000, random_seed: int = 12345):
    dw = math.sqrt(dt) * np.random.standard_normal(n_timestep)
    ds = (r - 0.5 * sigma**2) * dt + sigma * dw
    result = np.exp(np.cumsum(ds))
    return result


def get_renko(data: [float], delta: float = 0.02) -> [float]:
    """gets the values of a renko chart with box size delta

    :param data: the time series data to use for creating the renko plot
    :param delta: box size, default 0.02
    :return: the values of the renko chart with box size delta
    """
    first = data[0]

    n_bins_below = math.ceil((first - min(data)) / delta)
    n_bins_above = math.ceil((max(data) - first) / delta)
    bins_below = (first - i_ * delta for i_ in range(n_bins_below, 0, -1))
    bins_above_incl_first = (first + i_ * delta for i_ in range(n_bins_above+1))
    bins = [*bins_below, *bins_above_incl_first]
    cuts = pd.cut(data, bins, labels=False)

    result = list(
        itertools.chain.from_iterable(
            _process_bin(c_, cuts, i_)
            for i_, c_ in enumerate(cuts)
        )
    )

    return {'renko': result, 'binned_values': cuts}
