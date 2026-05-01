# Traktor Kontrol F1 Ableton controller scripts

Two versions - 2 and 4 channel.

Common features:

- Clip rect/session ring, with navigation:
  - `QUANT`=up `REVERSE`=down
  - `SYNC`=left `CAPTURE`=right
- Clip colour (closest match, using F1 indexed colour mode).
  - Dim colour for clip present paused/off.
  - Bright colour for playing.
  - White for triggered.
- Stop (bottom row) stops channel's clip.
- Fader = channel fader.
- Knob (`FILTER`) = channel pan (yes, pretty much useless).

Key feature:

- Can use multiple F1 devices in different parts of grid.

The smaller clip ring means you can use these like "decks", controlling different parts of your session. Oo yea nice. 

### Fine print
Built with a variety of free plan AI agents using [`ableton-control-surface-core`](https://pypi.org/project/ableton-control-surface-core/) pip package as reference/rough guide to the (*dang it bobby*) undocumented Python controller API.

Tested with Ableton 12.3.8.

The code for each script is 99.345876248% the same, paste changes between each, this is not a crime against software engineering, DRY-obsessed please chill.

### Setup
- Copy folder(s) to Ableton User Library, e.g. 
  - `~/Ableton/User Library/Remote Scripts/Kontrol_F1_2ch`
  - `~/Ableton/User Library/Remote Scripts/Kontrol_F1_4ch`
- Use NI Controller editor to apply template (`*.nckf1` file) to hardware device.

Open Ableton, go to settings:

- `Link, Tempo & MIDI` tab
- Set `Control Surface` to `Kontrol F1 2ch` or `Kontrol F1 4ch`
- Select your F1 device in input & output
- Repeat for each device

Recommend setting `Remote` in input/output ports also to use for custom control mapping e.g. to override knobs (in 4ch) or to use channels 3&4 for whatever (in 2ch).

## Kontrol_F1_4ch
Standard/typical 4 channel x 4 scene Ableton control.

- 4x4 session ring, all pads are clip triggers.
- Fader and pan for all channels.
- Apply `KontrolF1-4ch-ableton.nckf1` to F1.

## Kontrol_F1_2ch
Simpler 2 channel x 4 scene Ableton control.

The right channels are used as CCs which can be mapped to whatever. 

- 2x4 session ring, all pads are clip triggers.
- Fader and pan for channel 1+2 (i.e. ring).
- Apply `KontrolF1-2ch-ableton.nckf1` to F1.
- Hardware channels 3+4 on right are generic CCs:
  - knob
  - fader
  - 4x pad buttons

The idea is that the clips & devices in the 2 channels have samples, layers, chains to play larger chunk of song instrumentation, e.g. drums+bass or chords+pads+arp. 

Then you can use ch 3+4 to control synth or mix params for those layers, or to enable/disable layers. 

Examples: 

- Map 4x pads in ch3 to mute/enable kick | sub | perc | hats layers (playing in ch1).
- Map 4x pads in ch4 for momentary sends or stabs on lead layer.

### Key challenge with 2ch version - manual mappings don't follow session ring
If you move the session ring, the manual mappings don't follow.

Mitigation: always set each device to the same channel range, e.g.

- Kontrol F1 #1 - Ableton ch1-2, manual map params to those channels
- Kontrol F1 #2 - Ableton ch3-4, manual map params to those channels

If there's a way to automatically map these let me know, would make this way better. For example: ch3 knob is mapped (in python script) to first device param in leftmost session ring.

