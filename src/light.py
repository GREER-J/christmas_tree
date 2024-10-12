import numpy as np
from src.colour import Colour


class Light:
    def __init__(self, x_pos: float, y_pos: float, z_pos: float) -> None:
        self._x = x_pos
        self._y = y_pos
        self._z = z_pos

        self._colour = Colour(0, 0, 0)

    @property
    def rLNn(self):
        return np.array([[self._x], [self._y], [self._z]])

    @property
    def colour(self):
        return self._colour

    @property
    def status(self) -> bool:
        return False

    def set_colour(self, colour: Colour) -> None:
        self._colour = colour
