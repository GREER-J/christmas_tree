from src.colour import Colour


def test_colour_creation():
    red = 30
    green = 140
    blue = 250

    colour = Colour(red, green, blue)

    assert colour._red == red
    assert colour._green == green
    assert colour._blue == blue
