from src.colour import Colour


def test_colour_creation():
    red = 30
    green = 140
    blue = 250

    colour = Colour(red, green, blue)

    assert colour._red == red
    assert colour._green == green
    assert colour._blue == blue


def test_colour_equal():
    red = 30
    green = 140
    blue = 250

    c1 = Colour(red, green, blue)
    c2 = Colour(red+1, green-1, blue+2)
    c3 = Colour(red, green, blue)

    res1 = c1 == c2
    res2 = c1 == c3

    assert res1 == False
    assert res2 == True
