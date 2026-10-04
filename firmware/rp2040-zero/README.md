# ClaudePad · RP2040-Zero

Reference firmware for running **ClaudePad** on the Waveshare RP2040-Zero with CircuitPython.

The board presents itself as a standard USB HID keyboard and maps three physical switches to Claude Code's permission options.

[**BUILD GUIDE**](../../docs/build-rp2040-zero.md) · [**FIRMWARE**](code.py) · [**CIRCUITPYTHON**](https://circuitpython.org/board/waveshare_rp2040_zero/)

---

## RP2040-Zero

<div align="center">

<img width="960" height="578" alt="image" src="https://github.com/user-attachments/assets/bfe9b3c4-20a8-4da5-8ca5-5dd015e9da26" />


</div>

> The reference ClaudePad uses the **Waveshare RP2040-Zero**, a small RP2040 board with native USB-C.

### For this build, only four connections are needed:

<img width="874" height="634" alt="image" src="https://github.com/user-attachments/assets/1f62b89a-9a59-4e14-a094-0323b22fd9b4" />


> Use the labels printed on your board to confirm pin positions before soldering.

---

## Key mapping

| Button | GPIO | Sends | Claude Code |
|:---:|:---:|:---:|---|
| Left | `GP2` | `1` | Yes |
| Middle | `GP3` | `2` | Yes, always |
| Right | `GP4` | `3` | No |

All three switches share **GND**.

```text
         CLAUDEPAD

     ┌───────┬───────┬───────┐
     │   1   │   2   │   3   │
     │  YES  │ ALWAYS│   NO  │
     └───┬───┴───┬───┴───┬───┘
         │       │       │
        GP2     GP3     GP4
         │       │       │
         └───┬───┴───┬───┘
             │
            GND
```

---

## Install

### 1. Install CircuitPython

Download the latest **stable** CircuitPython release for the Waveshare RP2040-Zero:

**[Download CircuitPython for RP2040-Zero →](https://circuitpython.org/board/waveshare_rp2040_zero/)**

Hold **BOOT** while connecting the board over USB-C. Copy the downloaded `.uf2` file to the `RPI-RP2` drive.

After flashing, the board will reboot as:

```text
CIRCUITPY
```

### 2. Install Adafruit HID

Download the CircuitPython library bundle that matches your installed CircuitPython major version:

**[CircuitPython Library Bundles →](https://circuitpython.org/libraries)**

Copy:

```text
adafruit_hid/
```

into:

```text
CIRCUITPY/lib/
```

### 3. Install ClaudePad

Download [`code.py`](code.py) from this directory and copy it to the root of `CIRCUITPY`.

The finished drive should look like:

```text
CIRCUITPY/
│
├── code.py
│
└── lib/
    └── adafruit_hid/
```

ClaudePad will start automatically.

No application or ClaudePad-specific driver is required.

---

## Change the right key to Escape

The reference firmware sends:

```text
1    2    3
```

If you'd rather have the right button cancel the prompt with `Escape`, open [`code.py`](code.py) and change:

```python
Keycode.THREE
```

to:

```python
Keycode.ESCAPE
```

---

## Firmware

The source for this implementation is:

[`code.py`](code.py)

```text
GP2  ──►  1
GP3  ──►  2
GP4  ──►  3
GND  ──►  shared by all switches
```

For soldering, enclosure assembly, testing, and troubleshooting, see the **[complete RP2040-Zero build guide](../../docs/build-rp2040-zero.md)**.

---

<sub>ClaudePad · RP2040-Zero reference implementation · Created by [Ailyn Diaz](https://github.com/ailynux)</sub>
