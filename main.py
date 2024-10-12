import sys
from src.tree import Tree
from src.light import Light
import argparse
import random
from rpi_ws281x import *

# LED strip configuration:
LED_COUNT = 50     # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 65      # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Main function to initialize the tree and respond to SSH commands
def main():
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true',
                        help='clear the display on exit')
    parser.add_argument('light_index', type=int, nargs='?',
                        help='index of the light to turn on')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    # Instantiate the Tree object with generated coordinates and DummyNeoPixel strip
    tree_coords = [(random.randint(1, 100), random.randint(
        1, 100), random.randint(1, 100)) for _ in range(LED_COUNT)]
    tree = Tree(tree_coords, strip)

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    # Check if a light number was provided as an argument (via SSH command)
    if args.light_index is None:
        print("Error: Please provide a light number to turn on.")
        sys.exit(1)

    try:
        light_index = args.light_index
        if 0 <= light_index < tree.num_lights:
            # Turn on the specified light
            # Set light color to red
            tree.set_light_color(light_index, (255, 0, 0))
            tree.turn_on_light(light_index)
            print(f"Light {light_index} is now ON and held.")
        else:
            print("Error: Light index out of range.")
            sys.exit(1)
    except ValueError:
        print("Error: Invalid light number provided.")
        sys.exit(1)

    # Hold indefinitely to keep the light on
    try:
        while True:
            pass
    except KeyboardInterrupt:
        if args.clear:
            print("Clearing lights and terminating program.")
            for i in range(tree.num_lights):
                tree.turn_off_light(i)
            strip.show()
        sys.exit(0)


if __name__ == "__main__":
    main()
