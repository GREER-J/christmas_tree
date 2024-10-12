from src.light import Light


class Tree:
    def __init__(self, coordinates: list[tuple[float, float, float]], strip) -> None:
        self.strip = strip
        self.num_lights = len(coordinates)

        self._collection = [Light(light[0], light[1], light[2])
                            for light in coordinates]

    def update_strip(self):
        """Push the current state of all lights to the physical LED strip."""
        for i, light in enumerate(self._collection):
            self.strip[i] = light.colour
        self.strip.show()

    def set_light_color(self, index, color):
        """Set the color of a light, but do not physically turn it on yet."""
        if 0 <= index < len(self.lights):
            self.lights[index].set_color(color)

    def turn_on_light(self, index):
        """Turn on a specific light."""
        if 0 <= index < len(self._collection):
            self._collection[index].status = True
            self.update_strip()

    def turn_off_light(self, index):
        """Turn off a specific light."""
        if 0 <= index < len(self._collection):
            self._collection[index].status = False
            self.update_strip()

    def set_all_colors(self, color):
        """Set the color of all lights without turning them on."""
        for light in self._collection:
            light.set_colour(color)
