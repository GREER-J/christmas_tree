import pytest
import numpy as np
from src.light import Light


def test_light_creation():
    x = 5
    y = 2
    z = 10

    light = Light(x_pos=x, y_pos=y, z_pos=z)

    # Use np.array_equal to compare numpy arrays
    assert np.array_equal(light.rLNn, np.array([[x], [y], [z]]))

    # Check that the light is initially off
    assert light.status == False
