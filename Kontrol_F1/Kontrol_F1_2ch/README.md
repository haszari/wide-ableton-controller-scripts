# Kontrol F1 - 2 Track Control Surface

A 2-track variant of the Kontrol F1 control surface script for Ableton Live 12, using the `ableton.v3` API.

## Overview

- **Session:** 4×2 clip grid (4 scenes × 2 tracks), per-track stop, stop all clips, transport stop
- **Mixer:** Volume faders (2), pan knobs (4), send A/B controls (2×2 tracks)
- **Navigation:** Page scrolling for tracks and scenes

## Mapping Files

Two `.nckf1` mapping files with similar MIDI mappings but different LED colour schemes:

- `KontrolF1-2ch-ableton-sunset.nckf1` — sunset theme, assignabl controls use ch13
- `KontrolF1-2ch-ableton-ocean.nckf1` — ocean theme, assignable controls ch14

Each file has two pages: **Basic** and **Shift** (hold Shift to access).

## Channel Strategy

| Channel | Purpose | Routing |
|---------|---------|---------|
| **12** | Script-managed controls | Handled by Python control surface script |
| **13**, **14** | Assignable controls | For manual MIDI mapping in Live (allows 2× instances without conflicts) |

Ableton Live requires unique (CC, channel) pairs for every control — it doesn't route by device. Using ch13 for assignable controls allows two Kontrol F1 instances to coexist.

## Basic Page Controls

### Script-Managed (ch12)

| Control | MIDI | Python Element | Function |
|---------|------|----------------|----------|
| Filter1 | CC 2 | `send_controls[0][0]` | Pan knob ch1 |
| Filter2 | CC 3 | `send_controls[0][1]` | Pan knob ch2 |
| Filter3 | CC 4 | `send_controls[0][2]` | Pan knob ch3 |
| Filter4 | CC 5 | `send_controls[0][3]` | Pan knob ch4 |
| Volume1 | CC 6 | `track_faders[0][0]` | Volume fader ch1 |
| Volume2 | CC 7 | `track_faders[0][1]` | Volume fader ch2 |
| Volume3 | CC 8 | `track_faders[0][2]` | Volume fader ch3 |
| Volume4 | CC 9 | `track_faders[0][3]` | Volume fader ch4 |
| Mute1 | CC 52 | `send_b_encoders[0][0]` | ch1 Send B |
| Mute2 | CC 53 | `send_a_encoders[0][1]` | ch2 Send A |
| Mute3 | CC 54 | `send_b_encoders[0][1]` | ch2 Send B |
| Mute4 | CC 55 | `send_a_encoders[0][0]` | ch1 Send A |
| Sync | note 0 | `sync_button` | Move session ring left |
| Capture | note 1 | `capture_button` | Move session ring right |
| Quant | note 2 | `quant_button` | Move session ring up |
| Reverse | note 3 | `reverse_button` | Move session ring down |
| PadA1 | note 36 | `clip_buttons[0][0]` | Session ring clip col 1 row 1 |
| PadB1 | note 37 | `clip_buttons[1][0]` | Session ring clip col 1 row 2 |
| PadC1 | note 38 | `clip_buttons[2][0]` | Session ring clip col 1 row 3 |
| PadD1 | note 39 | `clip_buttons[3][0]` | Session ring clip col 1 row 4 |
| PadA2 | note 40 | `clip_buttons[0][1]` | Session ring clip col 2 row 1 |
| PadB2 | note 41 | `clip_buttons[1][1]` | Session ring clip col 2 row 2 |
| PadC2 | note 42 | `clip_buttons[2][1]` | Session ring clip col 2 row 3 |
| PadD2 | note 43 | `clip_buttons[3][1]` | Session ring clip col 2 row 4 |

### Send Mapping (Non-Linear)

The 4 bottom buttons (Mute1-4) are intentionally mapped non-linearly to sends:

```
Physical:  [Mute1] [Mute2] [Mute3] [Mute4]
           CC 52    CC 53    CC 54    CC 55

Sends:     ch1 B    ch2 A    ch2 B    ch1 A
```

This layout matches the physical button positions on the hardware. The Python code in `midi.py` defines the reordering:

```python
SEND_A_CCS = [[55, 53]]  # ch1 A, ch2 A
SEND_B_CCS = [[52, 54]]  # ch1 B, ch2 B
```

Typically the left channel is a drum deck, so default send is reverb, and right channel is leads, default send is delay, and reverb for right channel is next to delay. 

### Assignable (ch13) — for manual MIDI mapping

| Control | MIDI | Notes |
|---------|------|-------|
| PadA3 | CC 44 | Toggle button |
| PadB3 | CC 45 | Toggle button |
| PadC3 | CC 46 | Toggle button |
| PadD3 | CC 47 | Toggle button |
| PadA4 | CC 48 | Gate button |
| PadB4 | CC 49 | Gate button |
| PadC4 | CC 50 | Gate button |
| PadD4 | CC 51 | Gate button |

Column 3 is set up as toggle buttons for muting drum layers (manually mapped).

Column 4 is not currently used.

## Shift Page Controls

### Script-Managed (ch12)

| Control | MIDI | Python Element | Function |
|---------|------|----------------|----------|
| Mute1 | note 52 | `stop_buttons[0][0]` | Per-track stop ch1 |
| Mute2 | note 53 | `stop_buttons[0][1]` | Per-track stop ch2 |
| Mute3 | note 54 | `stop_all_clip_button` | Stop all clips |
| Mute4 | note 55 | `transport_stop_button` | Transport stop |

### Assignable (ch12) — available for manual MIDI mapping

| Control | MIDI | Notes |
|---------|------|-------|
| Filter1-4 | CCs 43-46 | Shift-mode knob values |
| Volume1-4 | CCs 6-9 | Same as basic (not remapped) |
| Quant | CC 13 | Shift-mode nav |
| Reverse | CC 15 | Shift-mode nav |
| Sync | CC 12 | Shift-mode nav |
| Size | CC 17 | Shift-mode nav |
| Type | CC 16 | Shift-mode nav |
| PadA1-D4 | CCs 51-58, 18-25 | Shift-mode pad remapping |


## Requirements

- Ableton Live 12+
- `ableton-control-surface-core-0.0.7` (v3 API)

## Installation

1. Copy the `Kontrol_F1_2ch` folder to Ableton's MIDI Remote Scripts directory
2. Select "Kontrol F1" as a control surface in Live's MIDI preferences
3. Load either `.nckf1` mapping file into the Kontrol F1 hardware via Traktor Kontrol Editor
4. Load other `.nckf1` mapping on to a second Kontrol F1 unit to allow use of the freely-assignable CCs without conflicts
