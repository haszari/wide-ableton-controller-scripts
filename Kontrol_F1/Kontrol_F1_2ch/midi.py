
# Config constants 
CLIP_RECT_CHANNELS = 2
CLIP_RECT_SCENES = 4


# MIDI mapping constants for Kontrol F1
MIDI_CHANNEL = 12 # aka 13 in Protokol

# Clip grid
# 2 channels only, first two rows
# x4 buttons using MIDI notes (starting at note 36)
CLIP_NOTE_START = 36  # C2

# Bottom stop buttons (shift mode: MIDI notes on ch12)
# 2 per-track stop buttons + 2 spare for stop-all-clips and transport-stop
SHIFT_CLIP_STOP_FIRST = 52
SHIFT_STOP_BUTTONS = [[SHIFT_CLIP_STOP_FIRST + i for i in range(2)]]  # [52, 53]

# Bottom stop buttons (non-shift mode: CCs on ch12)
# Repurposed as send encoders (2ch x 2 sends = 4 controls)
# Hardware layout: [ch1B] [ch2A] [ch2B] [ch1A]
CLIP_STOP_FIRST_CC = 52
SEND_A_CCS = [[CLIP_STOP_FIRST_CC + 3, CLIP_STOP_FIRST_CC + 1]]  # [55, 53] = ch1 A, ch2 A
SEND_B_CCS = [[CLIP_STOP_FIRST_CC + 0, CLIP_STOP_FIRST_CC + 2]]  # [52, 54] = ch1 B, ch2 B

# Spare bottom buttons (notes in shift mode, ch12)
STOP_ALL_CLIPS_NOTE = SHIFT_CLIP_STOP_FIRST + 2  # 54
TRANSPORT_STOP_NOTE = SHIFT_CLIP_STOP_FIRST + 3  # 55

# Track faders: 2 CC messages (CC 6-7) for 2 tracks
FADER_CC_START = 6
FADER_CCS = [[FADER_CC_START + track_idx for track_idx in range(2)]]

# Knobs - send controls: 4 CC messages (CC 2-5)
SEND_CC_START = 2
SEND_CCS = [[SEND_CC_START + track_idx for track_idx in range(4)]]

# Note numbers for session navigation buttons
SYNC_BUTTON = 0
CAPTURE_BUTTON = 1
QUANT_BUTTON = 2
REVERSE_BUTTON = 3
