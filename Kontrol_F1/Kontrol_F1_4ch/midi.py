# MIDI mapping constants for Kontrol F1

MIDI_CHANNEL = 12 # aka 13 in Protokol

# Clip grid: 4x4 buttons using MIDI notes (starting at note 36)
CLIP_NOTE_START = 36  # C2
# Stop buttons (bottom row), mapped to MIDI notes.
# Note numbers: 52..55 (E2..G2-ish depending on Live naming)
CLIP_STOP_START = 52

# Track faders: 4 CC messages (CC 6-9)
FADER_CC_START = 6

# Send controls: 4 CC messages (CC 2-5)
SEND_CC_START = 2

# and some other constants 
CLIP_RECT_CHANNELS = 4
CLIP_RECT_SCENES = 4

# Generate fader CC numbers
FADER_CCS = [[FADER_CC_START + track_idx for track_idx in range(4)]]

# Generate send CC numbers
SEND_CCS = [[SEND_CC_START + track_idx for track_idx in range(4)]]

# Stop buttons for each track (4x1 matrix)
STOP_BUTTONS = [[CLIP_STOP_START + i for i in range(4)]]

# Note numbers for the following buttons
SYNC_BUTTON = 0
CAPTURE_BUTTON = 1
QUANT_BUTTON = 2
REVERSE_BUTTON = 3
