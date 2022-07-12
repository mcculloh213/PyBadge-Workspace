# PyBadge Workspace

A code workspace for the [Adafruit PyBadge][pybadge].

## Description

The Adafruit PyBadge an all-in-one compact dev board programmable in CircuitPython. Full of features squeezed onto a 3 3⁄8 × 2 1⁄8 inch rounded credit card sized rectangle. It’s a perfect wearable badge, but can be used for many projects.

The PyBadge is powered by our favorite microcontroller, the ATSAMD51, with 512KB of flash and 192KB of RAM. There is an additional 2 MB of QSPI flash for file storage, handy for images, fonts, sounds, or game assets.

On the front, there is a 1.8” 160x128 color TFT display with dimmable backlight. There is fast DMA support for drawing, so updates are incredibly fast. There are also 8 silicone-top buttons: they are clicky but have a soft button top so they’re nice and grippy. The buttons are arranged to mimic a gaming handheld, with a d-pad, 2 menu-select buttons and 2 fire-action buttons. There are also 5 NeoPixel LEDs to dazzle or track activity.

On the back, there is a full Feather-compatible header socket set, so you can plug in any FeatherWing to expand the capabilities of the PyBadge. There are also 3 STEMMA connectors - two 3-pin with ADC/PWM capability and one 4-pin that connects to I2C - you can use this for Grove sensors as well.

For built-in sensors, there is a light sensor that points out the front, and a 3-axis accelerometer that can detect taps and free-fall. To make bleeps and bloops, there’s a built in buzzer-speaker. For projects where you need more volume, you can plug in an 8 ohm speaker.

You can power the PyBadge from any of Adafruit’s LiPoly batteries, but this 400mAh one is suggested. An on-off switch will save battery power when not in use. Or power the board from the Micro USB port - it will also charge the battery if one is attached.

![Adafruit QT Py SAMD21 pinout](static/img/Adafruit_QT_Py_SAMD21_pinout.png)

## Configuration

### Bootloader

This development board uses [CircuitPython][circuitpython] to program the ATSAMD51 microcontroller unit.

| Date                       | Current Firmware  |
|----------------------------|-------------------|
| June 14<sup>th</sup>, 2022 | [7.3.0][firmware] |

[pybadge]: https://www.adafruit.com/product/4200 "Adafruit PyBadge"
[learn]: https://learn.adafruit.com/adafruit-pybadge "Learn | Adafruit PyBadge"
[circuitpython]: https://circuitpython.org/ "CircuitPython"
[circuitpython-docs]: https://docs.circuitpython.org/en/latest/docs/index.html "CircuitPython | Docs"
[circuitpython-firmware]: https://circuitpython.org/board/pybadge/ "CircuitPython | PyBadge Firmware"
[firmware]: https://downloads.circuitpython.org/bin/pybadge/en_US/adafruit-circuitpython-pybadge-en_US-7.3.0.uf2 "CircuitPython v7.3.0"