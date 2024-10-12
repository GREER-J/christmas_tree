import pytest
import numpy as np
from src.light import Light
from src.colour import Colour


def test_light_creation():
    x = 5
    y = 2
    z = 10

    light = Light(x_pos=x, y_pos=y, z_pos=z)

    # Use np.array_equal to compare numpy arrays
    assert np.array_equal(light.rLNn, np.array([[x], [y], [z]]))
    assert light._colour == Colour(0, 0, 0)

    # Check that the light is initially off
    assert light.status == False


def test_turn_set_colour():
    colour = Colour(23, 45, 240)

    light = Light(23, 54, 56)
    light.set_colour(colour)

    assert light._colour == colour


def test_turn_get_colour():
    colour = Colour(23, 45, 240)

    light = Light(23, 54, 56)
    light.set_colour(colour)

    res = light._colour

    assert res == colour
