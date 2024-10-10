import numpy as np

class Light:
	def __init__(self, x_pos: float, y_pos: float, z_pos: float) -> None:
		self._x = x_pos
		self._y = y_pos
		self._z = z_pos

	@property
	def rLNn(self):
		return np.array([[self._x], [self._y], [self._z]])

	@property
	def status(self) -> bool:
		return False