from src.tree import Tree
from src.light import LightProtocol, Colour
import random


class DummyNeoPixel(LightProtocol):
    def __init__(self, pin, num_lights, auto_write=False):
        self.pin = pin
        self.num_lights = num_lights
        self.auto_write = auto_write
        self.show_called = False
        self.pixels = [(0, 0, 0)] * num_lights

    def __setitem__(self, index, color):
        if 0 <= index < self.num_lights:
            self.pixels[index] = color

    def show(self):
        self.show_called = True
        print(f"Displaying colors: {self.pixels}")


class DummyLight(LightProtocol):
    def __init__(self, x_pos, y_pos, z_pos, colour):
        pass

    def turn_off(self):
        self.turn_off_been_called = True

    def turn_on(self):
        self.turn_on_been_called = True

    def set_colour(self, colour):
        self.colour_was_set = colour


class DummyLightFactory:
    def create_light(self, x_pos: float, y_pos: float, z_pos: float) -> LightProtocol:
        return DummyLight(x_pos, y_pos, z_pos, Colour(0, 0, 0))


def test_tree_creation():
    num_lights = 10

    tree_coords = [(random.randint(1, 100), random.randint(
        1, 100), random.randint(1, 100)) for _ in range(num_lights)]

    strip = DummyNeoPixel(18, num_lights, False)
    tree = Tree(tree_coords, strip, DummyLightFactory())

    assert tree.num_lights == num_lights


def test_tree_calls_show():
    num_lights = 10

    tree_coords = [(random.randint(1, 100), random.randint(
        1, 100), random.randint(1, 100)) for _ in range(num_lights)]

    strip = DummyNeoPixel(18, num_lights, False)

    tree = Tree(tree_coords, strip, DummyLightFactory())
    tree.update_strip()

    assert strip.show_called == True


def test_tree_turns_lights_on():
    num_lights = 10
    tree_coords = [(random.randint(1, 100), random.randint(
        1, 100), random.randint(1, 100)) for _ in range(num_lights)]
    strip = DummyNeoPixel(18, num_lights, False)
    tree = Tree(tree_coords, strip, DummyLightFactory())

    tree.turn_on_light(3)

    assert tree._collection[3].turn_on_been_called == True


def test_tree_turns_lights_off():
    num_lights = 10
    tree_coords = [(random.randint(1, 100), random.randint(
        1, 100), random.randint(1, 100)) for _ in range(num_lights)]
    strip = DummyNeoPixel(18, num_lights, False)
    tree = Tree(tree_coords, strip, DummyLightFactory())

    tree.turn_off_light(3)

    assert tree._collection[3].turn_off_been_called == True


def test_tree_sets_colour():
    num_lights = 10
    tree_coords = [(random.randint(1, 100), random.randint(
        1, 100), random.randint(1, 100)) for _ in range(num_lights)]
    strip = DummyNeoPixel(18, num_lights, False)
    tree = Tree(tree_coords, strip, DummyLightFactory())

    tree.set_light_color(3, Colour(1, 2, 3))

    assert tree._collection[3].colour_was_set == Colour(1, 2, 3)
