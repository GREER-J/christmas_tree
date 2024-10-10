# Christmas Tree localisation
Inspired by Matt Parker's similar project to localise LEDs on a christmas tree.

## Plan
I'd like to localise the 3d positions of the light in space. For a first pass I'd like to use this laptops camera to find the height of the LEDs then I can turn them on and off in sequence according to height

The loop I'll be moving towards will be:
1. Order the raspberry pi (via ssh) to turn on a specific light
2. Take a photo of the scene with the laptops camera
3. Find the brightest object in that scene and assume it's the light
4. Create a light object and assign it the height coordinate proportional to the height of the pixel
5. Add the light to a structure of lights
6. Create a wave pattern that uses that structure to turn on and off lights according to z height