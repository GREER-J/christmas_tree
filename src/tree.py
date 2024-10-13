from src.light import LightFactory, LightProtocol
from src.colour import Colour


class Tree:
    def __init__(self, coordinates: list[tuple[float, float, float]], strip, light_factory: LightFactory) -> None:
        self.strip = strip
        self.num_lights = len(coordinates)

        self._collection = [light_factory.create_light(
            pos[0], pos[1], pos[2]) for pos in coordinates]

    def update_strip(self):
        """Push the current state of all lights to the physical LED strip."""
        for i, light in enumerate(self._collection):
            color = Color(light.to_RBG())
            self.strip.setPixelColor(i, color)
        self.strip.show()

    def set_light_color(self, index, colour: Colour):
        """Set the color of a light, but do not physically turn it on yet."""
        if 0 <= index < len(self._collection):
            self._collection[index].set_colour(colour)

    def turn_on_light(self, index):
        """Turn on a specific light."""
        if 0 <= index < len(self._collection):
            self._collection[index].turn_on()
            self.update_strip()

    def turn_off_light(self, index):
        """Turn off a specific light."""
        if 0 <= index < len(self._collection):
            self._collection[index].turn_off()
            self.update_strip()

    def set_all_colors(self, color):
        """Set the color of all lights without turning them on."""
        for light in self._collection:
            light.set_colour(color)
