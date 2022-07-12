import neopixel as _np
from adafruit_led_animation import animation as _anim, color as colors
from adafruit_led_animation.animation.blink import Blink
from pybadge import math

NeoPixel = _np.NeoPixel
RGB = _np.RGB
GRB = _np.GRB
RGBW = _np.RGBW
GRBW = _np.GRBW

Animation = _anim.Animation

NEOPIXEL_OFF = colors.BLACK


def stop_running_animation(animation: Animation):
    animation.freeze()
    animation.fill(NEOPIXEL_OFF)


class NeoPixelDriver:
    @property
    def pixel0(self):
        """The left-most NeoPixel"""
        return self.__neopixels[0]

    @pixel0.setter
    def pixel0(self, value: tuple):
        self.__neopixels[0] = value

    @property
    def pixel1(self):
        """The second-left NeoPixel"""
        return self.__neopixels[1]

    @pixel1.setter
    def pixel1(self, value: tuple):
        self.__neopixels[1] = value

    @property
    def pixel2(self):
        """The center NeoPixel"""
        return self.__neopixels[2]

    @pixel2.setter
    def pixel2(self, value: tuple):
        self.__neopixels[2] = value

    @property
    def pixel3(self):
        """The second-right NeoPixel"""
        return self.__neopixels[3]

    @pixel3.setter
    def pixel3(self, value: tuple):
        self.__neopixels[3] = value

    @property
    def pixel4(self):
        """The right-most NeoPixel"""
        return self.__neopixels[4]

    @pixel4.setter
    def pixel4(self, value: tuple):
        self.__neopixels[4] = value

    @property
    def pixels(self) -> NeoPixel:
        return self.__neopixels
    
    @property
    def animation(self) -> Animation or None:
        return self.__animation
    
    @animation.setter
    def animation(self, value: Animation or None):
        self.__animation = value

    def __init__(self, neopixels: NeoPixel):
        """
        PyBoard NeoPixel Driver

        :param neopixels: the PyBoard built-in NeoPixels
        :type neopixels: NeoPixel
        """
        self.__neopixels = neopixels
        self.__animation = None

    def set_brightness(self, value: float):
        """
        Sets the brightness of the PyBoard NeoPixels.
        :param value: brightness value between 0 and 1.
        :type value: float
        """
        self.pixels.brightness = math.minmax(value, 0., 1.)
        self.write()

    def write(self):
        """
        Call the associated write function to display the pixels
        """
        self.pixels.show()

    def animate(self):
        if self.animation is not None:
            self.animation.animate()

    def stop_animation(self):
        if self.animation is not None:
            stop_running_animation(self.animation)
            self.animation = None

    def stop_animation_when_complete(self):
        if self.animation is not None:
            self.animation.add_cycle_complete_receiver(stop_running_animation)

    def render(self):
        if self.animation is not None:
            self.animation.animate()
        else:
            self.write()

    def blink(self, speed: float, color: tuple or int):
        self.stop_animation()
        self.animation = Blink(self.pixels, speed, color, name="BlinkAnim")
