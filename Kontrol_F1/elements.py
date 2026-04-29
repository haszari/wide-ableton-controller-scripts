from ableton.v3.control_surface import ElementsBase
from ableton.v3.control_surface import MIDI_NOTE_TYPE, MIDI_CC_TYPE
from .midi import MIDI_CHANNEL, CLIP_BUTTONS, FADER_CCS, SEND_CCS


class Elements(ElementsBase):

    def __init__(self, *a, **k):
        super().__init__(global_channel=MIDI_CHANNEL, *a, **k)

        # Clip grid buttons (4x4) on Channel 0
        self.add_button_matrix(CLIP_BUTTONS, 'clip_buttons', 
                              msg_type=MIDI_NOTE_TYPE, 
                              is_momentary=True)

        # Track faders (4) on Channel 13
        self.add_encoder_matrix(FADER_CCS, 'track_faders',
                               msg_type=MIDI_CC_TYPE)

        # Send controls (4) on Channel 12
        self.add_encoder_matrix(SEND_CCS, 'send_controls',
                               msg_type=MIDI_CC_TYPE)
