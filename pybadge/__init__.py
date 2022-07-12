import board
from pybadge import gamepad, light, neopixel

__NEOPIXEL_COUNT: int = 5
__NEOPIXELS: neopixel.NeoPixel = neopixel.NeoPixel(
    board.NEOPIXEL, __NEOPIXEL_COUNT, brightness=1, pixel_order=neopixel.GRB
)
neopixel_driver = neopixel.NeoPixelDriver(__NEOPIXELS)

__SHIFT_REGISTER_KEYS = gamepad.ShiftRegisterKeys(
    clock=board.BUTTON_CLOCK,
    data=board.BUTTON_OUT,
    latch=board.BUTTON_LATCH,
    key_count=8,
    value_when_pressed=True,
)
gamepad_driver = gamepad.GamepadDriver(__SHIFT_REGISTER_KEYS)

__ANALOG_LIGHT_SENSOR = light.AnalogIn(board.A7)
light_sensor = light.AnalogLightSensor(__ANALOG_LIGHT_SENSOR)
