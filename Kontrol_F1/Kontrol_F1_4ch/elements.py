from ableton.v3.control_surface import ElementsBase
from ableton.v3.control_surface import MIDI_NOTE_TYPE, MIDI_CC_TYPE
from .midi import (
    CLIP_RECT_CHANNELS,
    CLIP_RECT_SCENES,
    MIDI_CHANNEL,
    CLIP_NOTE_START,
    FADER_CCS,
    SEND_CCS,
    STOP_BUTTONS,
    SYNC_BUTTON,
    CAPTURE_BUTTON,
    QUANT_BUTTON,
    REVERSE_BUTTON,
)


class Elements(ElementsBase):

    def __init__(self, *a, **k):
        super().__init__(global_channel=MIDI_CHANNEL, *a, **k)

        clip_grid_midi = []
        for scene_idx in range(CLIP_RECT_SCENES):
            row = []
            for channel_idx in range(CLIP_RECT_CHANNELS):
                row.append(CLIP_NOTE_START + scene_idx + channel_idx*CLIP_RECT_SCENES)
            clip_grid_midi.append(row)

        # Clip grid buttons
        self.add_button_matrix(clip_grid_midi, 'clip_buttons', 
                              msg_type=MIDI_NOTE_TYPE, 
                              is_momentary=True)

        # Bottom stop buttons (1x4) mapped to MIDI notes 52..55
        self.add_button_matrix(STOP_BUTTONS, 'stop_buttons',
                              msg_type=MIDI_NOTE_TYPE,
                              is_momentary=True)

        # Session navigation buttons (page scrolling).
        # You indicated these are sent as MIDI notes on the Kontrol F1.
        # - QUANT up / REVERSE down (move scenes by page size)
        # - SYNC left / CAPTURE right (move tracks by page size)
        self.add_button(QUANT_BUTTON, 'quant_button', msg_type=MIDI_NOTE_TYPE, is_momentary=True)
        self.add_button(REVERSE_BUTTON, 'reverse_button', msg_type=MIDI_NOTE_TYPE, is_momentary=True)
        self.add_button(SYNC_BUTTON, 'sync_button', msg_type=MIDI_NOTE_TYPE, is_momentary=True)
        self.add_button(CAPTURE_BUTTON, 'capture_button', msg_type=MIDI_NOTE_TYPE, is_momentary=True)

        # Track faders (4) on Channel 13
        self.add_encoder_matrix(FADER_CCS, 'track_faders',
                               msg_type=MIDI_CC_TYPE)

        # Send controls (4) on Channel 12
        self.add_encoder_matrix(SEND_CCS, 'send_controls',
                               msg_type=MIDI_CC_TYPE)
