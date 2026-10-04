# ClaudePad — RP2040-Zero Firmware
# Created by Ailyn Diaz (@ailynux)
# https://github.com/ailynux/ClaudePad
#
# A 3-key USB HID macropad for Claude Code permission prompts.
# Licensed under the MIT License. See LICENSE in the project root.

import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

pins = [board.GP2, board.GP3, board.GP4]
keys = [Keycode.ONE, Keycode.TWO, Keycode.THREE]  # yes / yes always / no

buttons = []

for p in pins:
    b = digitalio.DigitalInOut(p)
    b.switch_to_input(pull=digitalio.Pull.UP)
    buttons.append(b)

prev = [True] * 3

while True:
    for i, b in enumerate(buttons):
        v = b.value

        if prev[i] and not v:
            kbd.send(keys[i])

        prev[i] = v

    time.sleep(0.01)
