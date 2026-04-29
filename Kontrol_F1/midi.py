# MIDI mapping constants for Kontrol F1

MIDI_CHANNEL = 12 # aka 13 in Protokol

# Clip grid: 4x4 buttons using MIDI notes (starting at note 36)
CLIP_NOTE_START = 36  # C2
# the stop buttons currently have CCs mapped - need to update to buttons or use shift mode etc
CLIP_STOP_START = 51  

# Track faders: 4 CC messages (CC 6-9)
FADER_CC_START = 6

# Send controls: 4 CC messages (CC 2-5)
SEND_CC_START = 2

# Generate clip button note numbers (column-major: col1-1,col1-2,col1-3,col1-4, col2-1, etc.)
# Hardware expects: col1 has notes 36,40,44,48 (rows 1-4), col2 has 37,41,45,49, etc.
CLIP_BUTTONS = [
    [CLIP_NOTE_START + (row_idx * 4) + col_idx for row_idx in range(4)]
    for col_idx in range(4)
]

# Generate fader CC numbers
FADER_CCS = [[FADER_CC_START + track_idx for track_idx in range(4)]]

# Generate send CC numbers
SEND_CCS = [[SEND_CC_START + track_idx for track_idx in range(4)]]

