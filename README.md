<div align="center">

<pre>
 ██████╗██╗      █████╗ ██╗   ██╗██████╗ ███████╗██████╗  █████╗ ██████╗
██╔════╝██║     ██╔══██╗██║   ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗
██║     ██║     ███████║██║   ██║██║  ██║█████╗  ██████╔╝███████║██║  ██║
██║     ██║     ██╔══██║██║   ██║██║  ██║██╔══╝  ██╔═══╝ ██╔══██║██║  ██║
╚██████╗███████╗██║  ██║╚██████╔╝██████╔╝███████╗██║     ██║  ██║██████╔╝
 ╚═════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚═════╝
</pre>

### three keys. one job.

A USB-C macropad built for Claude Code permission prompts.
No app. No drivers. Just three switches and an RP2040-Zero.

</div>

<div align="center">

<table>
<tr>
<td align="center" width="150">
<kbd>&nbsp;&nbsp; 1 &nbsp;&nbsp;</kbd><br>
<sub><b>YES</b></sub>
</td>
<td align="center" width="150">
<kbd>&nbsp;&nbsp; 2 &nbsp;&nbsp;</kbd><br>
<sub><b>YES, ALWAYS</b></sub>
</td>
<td align="center" width="150">
<kbd>&nbsp;&nbsp; 3 &nbsp;&nbsp;</kbd><br>
<sub><b>NO</b></sub>
</td>
</tr>
</table>

**[BUILD](docs/build-rp2040-zero.md)** &nbsp;·&nbsp;
**[FIRMWARE](firmware/rp2040-zero/code.py)** &nbsp;·&nbsp;
**[3D MODEL](https://makerworld.com/en/models/2661831-claude-code-keyboard#profileId-2944520)**

![CircuitPython](https://img.shields.io/badge/CircuitPython-000?style=flat-square&logo=circuitpython&logoColor=fff)
![RP2040-Zero](https://img.shields.io/badge/RP2040--ZERO-000?style=flat-square)
![USB HID](https://img.shields.io/badge/USB-HID-000?style=flat-square)
![Open Hardware](https://img.shields.io/badge/BOARD_PORTS-WELCOME-000?style=flat-square)
</div>


<br>

<div align="center">
<img width="1440" height="1320" alt="image" src="https://github.com/user-attachments/assets/59e9d9a2-882a-4544-9ea1-012976f79a39" />
</div>

<br>

> Claude asks for permission.  
> I wanted a button for that.

---

## The idea

ClaudePad does one thing: **turn Claude Code permission prompts into physical buttons.**

The reference build runs **CircuitPython** on a **Waveshare RP2040-Zero** and presents itself as a standard USB keyboard. No companion app. No drivers. No background process.

Just three switches and USB.

```text
╭──────────────────────────────────────────────────────╮
│                     CLAUDE CODE                      │
│                                                      │
│                  Permission required                 │
│                                                      │
│        ┌─────────┐   ┌─────────┐   ┌─────────┐       │
│        │    1    │   │    2    │   │    3    │       │
│        │   YES   │   │  ALWAYS │   │    NO   │       │
│        └────┬────┘   └────┬────┘   └────┬────┘       │
│             │             │             │            │
╰─────────────┼─────────────┼─────────────┼────────────╯
              │             │             │
              └─────────────┼─────────────┘
                            │
                         USB HID
                            │
                            ▼
                   ┌─────────────────┐
                   │   RP2040-ZERO   │
                   │  CIRCUITPYTHON  │
                   └────────┬────────┘
                            │
                            ▼
                       your machine
```

**Claude asks. You press the button.**

---

## Build the reference version

<div align="center">

### RP2040-Zero + CircuitPython

The original ClaudePad implementation.

[**OPEN THE BUILD GUIDE →**](docs/build-rp2040-zero.md)

</div>

<br>

| | Reference build |
|---|---|
| Controller | Waveshare RP2040-Zero |
| Runtime | CircuitPython |
| Interface | USB HID |
| Inputs | 3 mechanical switches |
| GPIO | GP2 · GP3 · GP4 |
| Enclosure | 3D printed |
| Custom PCB | Not required |

The build guide contains the parts list, CircuitPython setup, HID library installation, pin testing, wiring, soldering, assembly, and troubleshooting.

The actual firmware stays separate:

```text
firmware/rp2040-zero/code.py
```

[View firmware →](firmware/rp2040-zero/code.py)

---

## Gallery

<div align="center">

<img width="1440" height="1052" alt="image" src="https://github.com/user-attachments/assets/37da67bb-11b4-4837-9ac6-80e66e905a1e" />

</div>

<!--
Have a good video clip?

Convert a short 3–6 second demo to a reasonably sized GIF and add:

<div align="center">
  <img src="assets/claudepad-demo.gif" width="820" alt="ClaudePad demo">
</div>

A clip of:
Claude permission prompt -> hand presses key -> prompt disappears
would look fantastic here.
-->

---

## Bring another board

The RP2040-Zero is the **reference implementation**, not the definition of ClaudePad.

If another microcontroller can expose itself as a keyboard and read three switches, there's probably a ClaudePad port waiting to happen.

```text
firmware/
│
├── rp2040-zero/
│   ├── code.py
│   └── README.md
│
└── your-board-here/
    ├── ...
    └── README.md
```

If you port it, send a PR.

Board implementations should keep their setup, pin mapping, dependencies, and board-specific notes inside their own directory instead of expanding the root README.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the conventions.

---

## The enclosure

<div align="center">

**The case isn't mine — but it is really damn good.**

[**CLAUDE CODE KEYBOARD · MAKERWORLD →**](https://makerworld.com/en/models/2661831-claude-code-keyboard#profileId-2944520)

</div>

<br>

The reference build uses the **Claude Code Keyboard** 3D model published on MakerWorld.

The model is not redistributed in this repository. Grab it directly from the original listing for the files, creator information, print settings, and license.

This repo starts where the print ends: controller, switches, wiring, firmware, and getting the thing talking to Claude Code.

---

## Links

| Resource | |
|---|---|
| RP2040-Zero build | [Build guide](docs/build-rp2040-zero.md) |
| Firmware | [`code.py`](firmware/rp2040-zero/code.py) |
| CircuitPython | [RP2040-Zero download](https://circuitpython.org/board/waveshare_rp2040_zero/) |
| HID library | [Adafruit CircuitPython HID](https://github.com/adafruit/Adafruit_CircuitPython_HID) |
| Enclosure | [MakerWorld model](https://makerworld.com/en/models/2661831-claude-code-keyboard#profileId-2944520) |

---

## Credits

**Firmware, electronics & documentation**  
[Ailyn Diaz](https://github.com/ailynux)

**Enclosure**  
[Claude Code Keyboard on MakerWorld](https://makerworld.com/en/models/2661831-claude-code-keyboard#profileId-2944520) — external model used by the reference build.

**Built with**  
[CircuitPython](https://circuitpython.org/) · [Adafruit CircuitPython HID](https://github.com/adafruit/Adafruit_CircuitPython_HID)

---

<div align="center">

<pre>
┌───────────────────────────────────────────────┐
│                                               │
│      CLAUDE ASKS.  YOU PRESS THE BUTTON.      │
│                                               │
└───────────────────────────────────────────────┘
</pre>

Built by [@ailynux](https://github.com/ailynux)

<sub>Independent community project.</sub>

</div>
