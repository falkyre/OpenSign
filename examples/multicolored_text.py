#!/usr/bin/env python
import time
from opensign import OpenSign
from opensign.canvas import OpenSignCanvas


def main():
    message = OpenSignCanvas()
    message.add_font("dejavu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    message.add_text("Hello ", color=(255, 0, 0))
    message.add_text("World!", color=(128, 255, 0))

    #sign = OpenSign(chain=6)
    sign = OpenSign(rows=32, columns=128, rgb_sequence="rbg",  gpio_mapping="adafruit-hat-pwm")
    while True:
        sign.scroll_in_from_left(message)
        time.sleep(1)
        sign.scroll_out_to_right(message)
        time.sleep(1)


# Main function
if __name__ == "__main__":
    main()
