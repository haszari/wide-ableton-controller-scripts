
# Config constants 
CLIP_RECT_CHANNELS = 2
CLIP_RECT_SCENES = 4


# MIDI mapping constants for Kontrol F1
MIDI_CHANNEL = 12 # aka 13 in Protokol

################################################################
# Clip grid
# 2 channels only, first two rows

# 2x4 buttons using MIDI notes (starting at note 36)
CLIP_NOTE_START = 36  # C2

# Bottom stop buttons
# 2 per-track stop buttons
CLIP_STOP_FIRST = 52
STOP_BUTTONS = [[52, 53]]

# shift mode - -all-clips and transport-stop
STOP_ALL_CLIPS_NOTE = 54
TRANSPORT_STOP_NOTE = 55

# Track faders: 2 CC messages (CC 6-7) for 2 tracks
FADER_CC_START = 6
FADER_CCS = [[FADER_CC_START + track_idx for track_idx in range(2)]]

# Knobs - send controls: 4 CC messages (CC 2-5)
SEND_CC_START = 2
SEND_CCS = [[SEND_CC_START + track_idx for track_idx in range(2)]]

################################################################
# Sends + mappable control section
# right two channels, CCs 

# Bottom stop buttons (non-shift mode: CCs on ch12)
# Repurposed as send encoders (2ch x 2 sends = 4 controls)
# Hardware layout: [ch2A, ch1B] 
#            shift [ch2B, ch1A]
# i.e. lead delay + drums reverb, and other sends for shift
SEND_A_CCS = [[53, 54]] 
SEND_B_CCS = [[55, 52]] 

# Note numbers for session navigation buttons
SYNC_BUTTON = 0
CAPTURE_BUTTON = 1
QUANT_BUTTON = 2
REVERSE_BUTTON = 3
