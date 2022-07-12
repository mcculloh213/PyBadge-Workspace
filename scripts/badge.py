import time
from adafruit_pybadger import pybadger

SAP_GREEN_RGB = (0x44, 0x76, 0x04)
ATOMIC_TANGERINE_RGB = (0xF6, 0x8E, 0x5F)
MANATEE_RGB = (0x8E, 0x9A, 0xAF)
MAGIC_MINT_RGB = (0xB3, 0xF2, 0xDD)
INDIGO_DYE_RGB = (0x18, 0x43, 0x5A)

LIGHT_INDEX = 0

def set_pixels(pixels, color):
    pixels[0] = color
    pixels[1] = color
    pixels[2] = color
    pixels[3] = color
    pixels[4] = color
    pixels.write()

def cycle_pixels(pixels):
    for i in range(4 * 5):
        for j in range(5):
            pixels[j] = (0, 0, 0)
        pixels[i % 5] = (255, 255, 255)
        pixels.write()
        time.sleep(0.1)

def bounce_pixels(pixels):
    for i in range(4 * 5):
        for j in range(5):
            pixels[j] = (0, 0, 128)
        if (i // 5) % 2 == 0:
            pixels[i % 5] = (0, 0, 0)
        else:
            pixels[5 - 1 - (i % 5)] = (0, 0, 0)
        pixels.write()
        time.sleep(0.1)

def fade_pixels(pixels):
    for i in range(0, 4 * 256, 8):
        for j in range(5):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            pixels[j] = (val, val, val)
        pixels.write()
        time.sleep(0.1)

def clear_pixels(pixels):
    for i in range(5):
        pixels[i] = (0, 0, 0)
    pixels.write()

def cycle_lights(pixels):
    global LIGHT_INDEX
    if LIGHT_INDEX == 0:
        set_pixels(pixels, SAP_GREEN_RGB)
    elif LIGHT_INDEX == 1:
        set_pixels(pixels, ATOMIC_TANGERINE_RGB)
    elif LIGHT_INDEX == 2:
        set_pixels(pixels, MANATEE_RGB)
    elif LIGHT_INDEX == 3:
        set_pixels(pixels, ATOMIC_TANGERINE_RGB)
    elif LIGHT_INDEX == 4:
        set_pixels(pixels, MAGIC_MINT_RGB)
    elif LIGHT_INDEX == 5:
        set_pixels(pixels, INDIGO_DYE_RGB)
    elif LIGHT_INDEX == 6:
        cycle_pixels(pixels)
    elif LIGHT_INDEX == 7:
        bounce_pixels(pixels)
    elif LIGHT_INDEX == 8:
        fade_pixels(pixels)
    else:
        clear_pixels(pixels)
    LIGHT_INDEX = (LIGHT_INDEX + 1) % 10

if __name__ == '__main__':
    pybadger.show_badge(
        background_color=SAP_GREEN_RGB,
        foreground_color=MAGIC_MINT_RGB,
        foreground_text_color=ATOMIC_TANGERINE_RGB,
        hello_string='Salve!',
        hello_scale=1,
        my_name_is_string='Mihi nomen est',
        my_name_is_scale=1,
        name_string='Chip',
        name_scale=3
    )

    while True:
        pybadger.auto_dim_display(delay=10)
        if pybadger.button.a:
            pybadger.show_business_card(
                image_name='porygon.bmp',
                name_string='Chip',
                name_scale=2,
                email_string_one='hdmccullough@gmail.com',
                email_string_two='',
            )
        elif pybadger.button.b:
            pybadger.show_qr_code(data='https://github.com/mcculloh213')
        elif pybadger.button.start:
            pybadger.show_badge(
                background_color=SAP_GREEN_RGB,
                foreground_color=MAGIC_MINT_RGB,
                foreground_text_color=ATOMIC_TANGERINE_RGB,
                hello_string='Salve!',
                hello_scale=1,
                my_name_is_string='Mihi nomen est',
                my_name_is_scale=1,
                name_string='Chip',
                name_scale=3
            )
        elif pybadger.button.select:
            cycle_lights(pybadger.pixels)
            time.sleep(1.0)
