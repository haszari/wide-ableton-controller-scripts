import Live
from ableton.v3.control_surface import ControlSurface, ControlSurfaceSpecification, Layer
from ableton.v3.control_surface.components import SessionComponent, MixerComponent, SessionNavigationComponent, TransportComponent
from .elements import Elements
from .skin import kontrol_f1_skin
from .midi import (
    CLIP_RECT_CHANNELS,
    CLIP_RECT_SCENES
)


"""
Kontrol F1 - Hello World Control Surface for Ableton Live 12
Basic script using ableton.v3 API with same MIDI settings as CustomControlSurface.py
"""

class Specification(ControlSurfaceSpecification):
    elements_type = Elements
    num_tracks = CLIP_RECT_CHANNELS
    num_scenes = CLIP_RECT_SCENES
    control_surface_skin = kontrol_f1_skin


class KontrolF1(ControlSurface):

    def __init__(self, c_instance=None):
        super().__init__(Specification(), c_instance=c_instance)

    def setup(self):
        super().setup()

        with self.component_guard():
            self._setup_session()
            self._setup_mixer()
            self._setup_transport()
            if self._session_ring:
                self._session_ring.set_enabled(True)

        self.application.view.add_focused_document_view_listener(self._on_view_changed)
        self._on_view_changed()

    def _setup_session(self):
        self._session = SessionComponent(name='Session', is_enabled=False, )
        self._session_navigation = SessionNavigationComponent(name='Session_Navigation', is_enabled=False)

        self._l1_session_layer = Layer(
            clip_launch_buttons='clip_buttons',
            stop_all_clips_button='stop_all_clip_button',
        )

        self._session.layer = self._l1_session_layer

        # Wire page-scroll controls:
        # Up (QUANT) / Down (REVERSE) moves scenes by page size (4).
        # Left (SYNC) / Right (CAPTURE) moves tracks by page size (4).
        self._session_navigation.set_page_up_button(self.elements.quant_button)
        self._session_navigation.set_page_down_button(self.elements.reverse_button)
        self._session_navigation.set_page_left_button(self.elements.sync_button)
        self._session_navigation.set_page_right_button(self.elements.capture_button)

        # Bottom stop buttons (notes 52..53) stop all clips for their track.
        # The order must match the track index (0..1).
        self._session.set_stop_track_clip_buttons(self.elements.stop_buttons_raw)

    def _setup_mixer(self):
        self._mixer = MixerComponent(name='Mixer', is_enabled=False, )

        self._l1_mixer_layer = Layer(
            volume_controls='track_faders',
            pan_controls='send_controls',
            send_a_control='send_a_encoders',
            send_b_control='send_b_encoders',
        )

        self._mixer.layer = self._l1_mixer_layer

    def _setup_transport(self):
        self._transport = TransportComponent(name='Transport', is_enabled=False)
        self._transport.layer = Layer(stop_button='transport_stop_button')
        self._transport.set_enabled(True)

    def _enter_session_mode(self):
        self._session.set_enabled(True)
        self._mixer.set_enabled(True)
        self._session_navigation.set_enabled(True)

    def _on_view_changed(self):
        view = self.application.view.focused_document_view
        is_arranger = (view == 'Arranger')

        self._enter_session_mode()

    def disconnect(self):
        super().disconnect()
