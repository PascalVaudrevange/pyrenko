import math
import numpy as np
import pandas as pd
import pytest


@pytest.fixture()
def data():
    r = 0.05
    sigma = 0.2
    dt = 0.0001
    n_timestep = 10000
    np.random.seed(12345)
    dw = math.sqrt(dt) * np.random.standard_normal(n_timestep)
    ds = (r - 0.5 * sigma**2) * dt + sigma * dw
    s = np.exp(np.cumsum(ds))
    result = pd.DataFrame({
        'value': s
    })
    return result


