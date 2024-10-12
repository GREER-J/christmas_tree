import numpy as np
from src.colour import Colour

import numpy as np

from typing import Protocol


class LightProtocol(Protocol):
    def __init__(self, x_pos: float, y_pos: float, z_pos: float, colour: Colour) -> None:
        ...

    @property
    def rLNn(self) -> np.ndarray:
        ...

    @property
    def colour(self) -> Colour:
        ...

    @property
    def status(self) -> bool:
        ...

    def set_colour(self, colour: Colour) -> None:
        ...

    def turn_on(self) -> None:
        ...

    def turn_off(self) -> None:
        ...


class LightFactory:
    def create_light(self, x_pos: float, y_pos: float, z_pos: float) -> LightProtocol:
        # Logic to create a Light object, can be extended as needed
        return Light(x_pos, y_pos, z_pos, Colour(0, 0, 0))


class Light(LightProtocol):
    def __init__(self, x_pos: float, y_pos: float, z_pos: float, colour: Colour) -> None:
        self._x = x_pos
        self._y = y_pos
        self._z = z_pos

        self._colour = colour

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
