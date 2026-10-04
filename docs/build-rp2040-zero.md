# ClaudePad — RP2040-Zero Build Guide

Build the reference version of **ClaudePad**: a three-key USB-C macropad for Claude Code permission prompts, powered by a Waveshare RP2040-Zero and CircuitPython.

```text id="g8fks9"
LEFT             MIDDLE             RIGHT
  1                 2                 3
 YES           YES, ALWAYS            NO
```

> **Reference build:** This guide covers the RP2040-Zero version of ClaudePad. Other board implementations may use different pins, firmware, or setup steps.

---

## Parts and tools

| Item | Notes |
|---|---|
| 3D-printed case | [Claude Code Keyboard on MakerWorld](https://makerworld.com/en/models/2661831-claude-code-keyboard) |
| Waveshare RP2040-Zero | Native USB; presents itself as a keyboard |
| 3 mechanical switches | Kailh Blue in the reference build; 2-pin, no polarity |
| 6 wires, ~10 cm each | Two colors recommended: one for ground, one for signal |
| USB-C cable | Must support data, not charge-only |
| Soldering iron + solder | Sn63/Pb37 works fine; wash your hands after handling leaded solder |
| Wire strippers | For preparing the switch wires |
| Tape | Useful for labeling signal wires before soldering |
| Hot glue or double-sided tape | Holds the RP2040-Zero inside the enclosure |
| 3 keycaps | Install these last |

---

## 1. Flash CircuitPython

<img width="1440" height="920" alt="image" src="https://github.com/user-attachments/assets/f1f0e756-32e9-4f0c-ac4c-011bee9be8f0" />


No IDE or drivers are required.

1. Open the [CircuitPython page for the Waveshare RP2040-Zero](https://circuitpython.org/board/waveshare_rp2040_zero/) and download the latest **stable** `.uf2` release.

   Note the major version number. For example, if you download `10.3.1`, you'll need the `10.x` library bundle later.

2. Hold the **BOOT** button on the RP2040-Zero while plugging it into your computer over USB-C, then release the button.

   A drive named:

   ```text id="8ix2zj"
   RPI-RP2
   ```

   should appear.

3. Drag the downloaded `.uf2` file onto `RPI-RP2`.

   The board will reboot automatically and reappear as:

   ```text id="e3rz8c"
   CIRCUITPY
   ```

4. Open the [CircuitPython Libraries](https://circuitpython.org/libraries) page and download the bundle matching your CircuitPython major version.

   For CircuitPython `10.x`, for example, download the **Bundle for Version 10.x**.

5. Unzip the bundle and open its `lib` directory.

6. Copy the `adafruit_hid` folder into:

   ```text id="pjb8oq"
   CIRCUITPY/lib/
   ```

Only `adafruit_hid` is required for ClaudePad.

---

## 2. Load the firmware

Download [`code.py`](../firmware/rp2040-zero/code.py) from this repository and copy it to the root of the `CIRCUITPY` drive.

Your drive should look roughly like this:

```text id="8hfhdo"
CIRCUITPY/
├── code.py
└── lib/
    └── adafruit_hid/
```

CircuitPython automatically runs `code.py` when the board starts and reloads it when the file changes.

The reference firmware maps the three switches to:

| GPIO | Key | Claude Code action |
|---|---|---|
| GP2 | `1` | Yes |
| GP3 | `2` | Yes, always |
| GP4 | `3` | No |

> **Prefer Escape for the right key?**  
> Open `code.py` and replace `Keycode.THREE` with `Keycode.ESCAPE`.

---

## 3. Test before soldering

Test the board now. This confirms that CircuitPython, the HID library, and the firmware are working before any permanent wiring is involved.

1. Keep the RP2040-Zero plugged in.

2. Open a blank text file and click inside it so the cursor is active.

3. Hold the board with the **USB-C port pointing up** and the **chip facing you**.

   - `GND` is the second hole down on the left.
   - `GP2`, `GP3`, and `GP4` are the third, fourth, and fifth holes down on the right.

   The pin labels are also printed directly on the board.

4. Briefly bridge **GND → GP2** with a piece of wire.

   You should see:

   ```text id="1w8wnn"
   1
   ```

5. Repeat for the remaining pins:

   ```text id="ej6k2k"
   GND → GP2  =  1
   GND → GP3  =  2
   GND → GP4  =  3
   ```

> **Be careful:** Never bridge GND to `5V` or `3V3`, which are located nearby.

If all three keys register correctly, the firmware side is done.

---

## 4. Wire and solder

<img width="1440" height="1064" alt="image" src="https://github.com/user-attachments/assets/8cdced7a-7098-430b-a9ab-d5d302065707" />


Each switch needs two connections:

- one **signal** wire
- one **ground** wire

The three signal wires connect individually to `GP2`, `GP3`, and `GP4`. The three ground wires share the same `GND` connection.

### Wiring map

| Key from the front | Types | Signal | Ground |
|---|---:|---|---|
| Left | `1` | GP2 | GND |
| Middle | `2` | GP3 | GND |
| Right | `3` | GP4 | GND |

<img width="874" height="634" alt="image" src="https://github.com/user-attachments/assets/dc585363-254b-4cb7-8008-e73c329f1c22" />

<img width="1440" height="1656" alt="image" src="https://github.com/user-attachments/assets/e01e08a6-e24b-4838-879c-36e2caa6b884" />


### Soldering

1. Cut **6 wires** approximately 10 cm long and strip about 3–4 mm from each end.

   Using one color for ground and another for signal makes the wiring much easier to follow.

2. **Solder the wires to the switches before installing the switches in the case.**

   Working on the switches outside the enclosure is easier and keeps the soldering iron away from the printed plastic.

   The switch pins have no polarity, so either pin can be ground. Just wire all three consistently.

3. Tin each wire before attaching it to a switch.

   Once positioned, the joint should only need a short touch from the iron. Excessive heat can damage the plastic switch housing.

4. Thread both wires from each switch through its opening in the enclosure, then click the switch into place.

5. Label the three signal wires with tape:

   ```text id="g5mm2i"
   GP2
   GP3
   GP4
   ```

   > **Watch the orientation:** When you're looking at the enclosure from the back, left and right are reversed. The switch on your left is the right-hand key when viewed from the front.

6. Join the three ground wires together.

   Twist the stripped ends, add a small amount of solder so they behave as one connection, and solder the bundle to **GND**.

   If all three wires are too thick to fit through the GND hole, connect one ground wire to the board and join the remaining grounds to it just outside the hole.

7. Connect the three signal wires:

   ```text id="xgr7e0"
   LEFT    → GP2
   MIDDLE  → GP3
   RIGHT   → GP4
   ```

8. Inspect the board carefully and make sure no solder bridges neighboring pins.

> **Keys backwards?** Don't immediately reach for the soldering iron. You can change the order of the `pins` list in `code.py` instead.

---

## 5. Test and assemble

Before closing everything up:

1. Plug ClaudePad into your computer.

2. Open a blank text file.

3. Press the keys from left to right.

   You should get:

   ```text id="oh7w1b"
   1 2 3
   ```

4. Place the RP2040-Zero inside the enclosure with the USB-C port aligned to the side opening.

5. Secure the board with a small amount of hot glue or double-sided tape.

   Keep adhesive away from:

   - the USB-C port
   - the **BOOT** button
   - the **RESET** button

6. Tuck the wires into the enclosure without pinching or sharply bending them.

7. Install the keycaps.

---

## 6. Use it with Claude Code

Plug ClaudePad in and start Claude Code normally.

When a permission prompt appears:

```text id="9svgbj"
┌────────────┬──────────────────┬────────────┐
│   LEFT     │      MIDDLE      │   RIGHT    │
│            │                  │            │
│     1      │        2         │     3      │
│    YES     │   YES, ALWAYS    │     NO     │
└────────────┴──────────────────┴────────────┘
```

Press the corresponding physical key.

That's it.

---

### Operating system notes:

**Windows**

> ClaudePad should appear automatically as a standard USB keyboard. No ClaudePad-specific driver or software is required.

**macOS**

> ClaudePad should also appear automatically as a standard USB keyboard. The first time you connect it, macOS may open **Keyboard Setup Assistant**. ClaudePad doesn't need to be configured there, so you can close the assistant.


---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| No `RPI-RP2` or `CIRCUITPY` drive | Charge-only USB-C cable | Try a cable that supports data |
| One key types nothing | Cold solder joint or incorrect GPIO | Reflow the joint and verify GP2, GP3, or GP4 |
| A key types continuously | Signal is shorted to GND | Check for solder bridges or exposed wire touching ground |
| Keys are in the wrong order | Left/right were reversed while wiring from the back | Reorder the `pins` list in `code.py` |
| Switch feels sticky after soldering | Switch housing may have been overheated | Replace the affected switch |
| Keyboard Setup Assistant appears | Normal behavior on first connection to some Macs | Close the assistant |

---

## Reference files

- [`code.py`](../firmware/rp2040-zero/code.py) — RP2040-Zero firmware
- [`firmware/rp2040-zero/README.md`](../firmware/rp2040-zero/README.md) — firmware notes and pin mapping
- [Claude Code Keyboard on MakerWorld](https://makerworld.com/en/models/2661831-claude-code-keyboard) — enclosure used by the reference build
- [Waveshare RP2040-Zero CircuitPython](https://circuitpython.org/board/waveshare_rp2040_zero/) — CircuitPython download
- [CircuitPython Library Bundles](https://circuitpython.org/libraries) — contains `adafruit_hid`

---

## Enclosure credit

<img width="1440" height="1320" alt="image" src="https://github.com/user-attachments/assets/3aa92bd5-7c65-436e-816a-6428e9918efe" />


The enclosure used for the reference build is the **Claude Code Keyboard** model published on MakerWorld.

The enclosure was not created by me and is not redistributed in this repository. Download it from the [original MakerWorld listing](https://makerworld.com/en/models/2661831-claude-code-keyboard) for the model files, creator information, print settings, and applicable license.

ClaudePad's firmware, electronics documentation, and build instructions are maintained separately in this repository.
