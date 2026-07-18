# Traktor Kontrol F1 - Ableton Live Controller Scripts

Control surface scripts for NI Traktor Kontrol F1 in Ableton Live 12+.

Built with [`ableton-control-surface-core`](https://pypi.org/project/ableton-control-surface-core/).

## Scripts

| Script | Tracks | Scenes | README |
|--------|--------|--------|--------|
| `Kontrol_F1_2ch` | 2 | 4 | [2ch docs](Kontrol_F1/Kontrol_F1_2ch/README.md) |
| `Kontrol_F1_4ch` | 4 | 4 | [4ch docs](Kontrol_F1/Kontrol_F1_4ch/README.md) |

## TO DO
For manual mappings, Ableton requires that each hardware control sends a unique midi message, _across all midi controllers_.

For 2x F1s that means if we want to manually map some controls that we have a default (control script auto) mapping for, we need to extend the script to handle multiple devices on multiple midi channels.

Example:

- F1 a on ch13
- F1 b on ch14
- both send same messages
- script maps faders to channel faders by default, so follows ring
  - this is set up ~twice in script, once per device
- this means
  - we get focus-ring-follow for fader mapping
  - AND 
  - we can optionally customise F1 b fader mapping without it mapping to F1 a fader also

This is because Ableton ignores the device/bus - ALL midi controllers on one bus. 

For now no problem, means I should just keep this in mind and use my manual mappings as I am currently.

But is a bit of a gotcha.