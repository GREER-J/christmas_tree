from src.tree import Tree
import random


def test_tree_creation():
    num_lights = 40
    tree_coords = [(random.randint(1, 100), random.randint(
        1, 100), random.randint(1, 100)) for _ in range(num_lights)]
    tree = Tree(tree_coords)

    assert tree.num_lights == num_lights
