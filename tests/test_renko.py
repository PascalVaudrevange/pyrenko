import math
import numpy as np
import pandas as pd
import pytest



@pytest.fixture()
def data():
    r = 0.05
    sigma = 0.25
    dt = 0.0001
    n_timestep = 10000
    result = get_data(r, sigma, dt, n_timestep)
    return result
