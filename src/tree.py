from src.light import Light


class Tree:
    def __init__(self, coordinates: list[tuple[float, float, float]]) -> None:
        self.num_lights = len(coordinates)
        self._collection = [Light(light[0], light[1], light[2])
                            for light in coordinates]
