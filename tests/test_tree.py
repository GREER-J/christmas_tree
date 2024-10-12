from src.tree import Tree
import random


class DummyNeoPixel:
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


def test_tree_creation():
    num_lights = 10

    tree_coords = [(random.randint(1, 100), random.randint(
        1, 100), random.randint(1, 100)) for _ in range(num_lights)]

    strip = DummyNeoPixel(18, num_lights, False)
    tree = Tree(tree_coords, strip)

    assert tree.num_lights == num_lights


def test_tree_calls_show():
    num_lights = 10

    tree_coords = [(random.randint(1, 100), random.randint(
        1, 100), random.randint(1, 100)) for _ in range(num_lights)]

    strip = DummyNeoPixel(18, num_lights, False)
    tree = Tree(tree_coords, strip)
    tree.update_strip()

    assert strip.show_called == True
