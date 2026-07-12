# Kontrol F1 - 4 Track Control Surface

Standard 4×4 Ableton Live control surface script.

This is not maintained, 2ch script has more features customised to my specific "2-deck" workflow.

## Features

- **Session:** 4×4 clip grid (4 scenes × 4 tracks), per-track stop buttons
- **Mixer:** Volume faders (4), pan knobs (4)
- **Navigation:** Page scrolling for tracks and scenes

## Controls

| Control | MIDI | Python Element | Function |
|---------|------|----------------|----------|
| Filter1-4 | CCs 2-5 | `send_controls` | Pan knobs ch1-4 |
| Volume1-4 | CCs 6-9 | `track_faders` | Volume faders ch1-4 |
| Mute1-4 | notes 52-55 | `stop_buttons` | Per-track stop ch1-4 |
| Sync | note 0 | `sync_button` | Page left |
| Capture | note 1 | `capture_button` | Page right |
| Quant | note 2 | `quant_button` | Page up |
| Reverse | note 3 | `reverse_button` | Page down |
| PadA1 | note 36 | `clip_buttons[0][0]` | Clip slot A1 |
| PadA2 | note 40 | `clip_buttons[0][1]` | Clip slot A2 |
| PadA3 | note 44 | `clip_buttons[0][2]` | Clip slot A3 |
| PadA4 | note 48 | `clip_buttons[0][3]` | Clip slot A4 |
| PadB1-D4 | notes 37-51 | `clip_buttons` | Remaining clip slots |

All controls on MIDI channel 12.

## Mapping File

Apply `KontrolF1-4ch-ableton.nckf1` to F1 hardware via NI Controller Editor.

## Installation

1. Copy `Kontrol_F1_4ch` folder to Ableton's MIDI Remote Scripts directory
2. Load `KontrolF1-4ch-ableton.nckf1` onto F1 hardware
3. Select "Kontrol F1 4ch" as control surface in Ableton MIDI preferences
