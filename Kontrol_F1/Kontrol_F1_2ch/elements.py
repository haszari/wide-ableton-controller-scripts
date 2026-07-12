from ableton.v3.control_surface import ElementsBase
from ableton.v3.control_surface import MIDI_NOTE_TYPE, MIDI_CC_TYPE
from .midi import (
    CLIP_RECT_CHANNELS,
    CLIP_RECT_SCENES,
    MIDI_CHANNEL,
    CLIP_NOTE_START,
    FADER_CCS,
    SEND_CCS,
    SEND_A_CCS,
    SEND_B_CCS,
    SHIFT_STOP_BUTTONS,
    STOP_ALL_CLIPS_NOTE,
    TRANSPORT_STOP_NOTE,
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

        # Bottom stop buttons (1x2) - per-track stop (shift mode: notes 52..53)
        self.add_button_matrix(SHIFT_STOP_BUTTONS, 'stop_buttons',
                              msg_type=MIDI_NOTE_TYPE,
                              is_momentary=True)

        # Session navigation buttons (page scrolling).
        self.add_button(QUANT_BUTTON, 'quant_button', msg_type=MIDI_NOTE_TYPE, is_momentary=True)
        self.add_button(REVERSE_BUTTON, 'reverse_button', msg_type=MIDI_NOTE_TYPE, is_momentary=True)
        self.add_button(SYNC_BUTTON, 'sync_button', msg_type=MIDI_NOTE_TYPE, is_momentary=True)
        self.add_button(CAPTURE_BUTTON, 'capture_button', msg_type=MIDI_NOTE_TYPE, is_momentary=True)

        # Track faders (2) 
        self.add_encoder_matrix(FADER_CCS, 'track_faders',
                               msg_type=MIDI_CC_TYPE)

        # Knob (pan) controls (4)
        self.add_encoder_matrix(SEND_CCS, 'send_controls',
                               msg_type=MIDI_CC_TYPE)

        # Send A/B stab controls (stop-button CCs repurposed as send encoders)
        # Hardware layout: [ch1B] [ch2A] [ch2B] [ch1A]
        self.add_encoder_matrix(SEND_A_CCS, 'send_a_encoders',
                               msg_type=MIDI_CC_TYPE)
        self.add_encoder_matrix(SEND_B_CCS, 'send_b_encoders',
                               msg_type=MIDI_CC_TYPE)

        # Spare bottom buttons for utility stop
        # Stop all clips
        self.add_button(STOP_ALL_CLIPS_NOTE, 'stop_all_clip_button',
                       msg_type=MIDI_NOTE_TYPE, is_momentary=True)
        # Stop transport
        self.add_button(TRANSPORT_STOP_NOTE, 'transport_stop_button',
                       msg_type=MIDI_NOTE_TYPE, is_momentary=True)
