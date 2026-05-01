import Live
from ableton.v3.control_surface import ControlSurface, ControlSurfaceSpecification, Layer
from ableton.v3.control_surface.components import SessionComponent, MixerComponent, SessionNavigationComponent
from .elements import Elements
from .skin import kontrol_f1_skin
from .midi import (
    CLIP_RECT_CHANNELS,
    CLIP_RECT_SCENES
)
# HSB mode custom component - unused/untested, kept for future reference
# from .clip_slot import KontrolF1ClipSlotComponent


"""
Kontrol F1 - Hello World Control Surface for Ableton Live 12
Basic script using ableton.v3 API with same MIDI settings as CustomControlSurface.py
"""

class Specification(ControlSurfaceSpecification):
    elements_type = Elements
    num_tracks = CLIP_RECT_CHANNELS
    num_scenes = CLIP_RECT_SCENES
    control_surface_skin = kontrol_f1_skin
    # HSB mode custom component - unused/untested
    # clip_slot_component_type = KontrolF1ClipSlotComponent


class KontrolF1(ControlSurface):

    def __init__(self, c_instance=None):
        super().__init__(Specification(), c_instance=c_instance)
        # self.log_message("Kontrol F1 Hello World - Control Surface initialized")

    def setup(self):
        super().setup()

        with self.component_guard():
            self._setup_session()
            self._setup_mixer()
            if self._session_ring:
                self._session_ring.set_enabled(True)

        self.application.view.add_focused_document_view_listener(self._on_view_changed)
        self._on_view_changed()

        # self.log_message("Kontrol F1 setup complete")

    def _setup_session(self):
        self._session = SessionComponent(name='Session', is_enabled=False, )
        self._session_navigation = SessionNavigationComponent(name='Session_Navigation', is_enabled=False)

        self._l1_session_layer = Layer(clip_launch_buttons='clip_buttons')

        self._session.layer = self._l1_session_layer

        # Wire page-scroll controls:
        # Up (QUANT) / Down (REVERSE) moves scenes by page size (4).
        # Left (SYNC) / Right (CAPTURE) moves tracks by page size (4).
        self._session_navigation.set_page_up_button(self.elements.quant_button)
        self._session_navigation.set_page_down_button(self.elements.reverse_button)
        self._session_navigation.set_page_left_button(self.elements.sync_button)
        self._session_navigation.set_page_right_button(self.elements.capture_button)

        # Bottom stop buttons (notes 52..55) stop all clips for their track.
        # The order must match the track index (0..3).
        self._session.set_stop_track_clip_buttons(self.elements.stop_buttons_raw)

    def _setup_mixer(self):
        self._mixer = MixerComponent(name='Mixer', is_enabled=False, )

        self._l1_mixer_layer = Layer(
            volume_controls='track_faders',
            pan_controls='send_controls',
        )

        self._mixer.layer = self._l1_mixer_layer

        # self._update_sends('l1')

    def _enter_session_mode(self):
        self._session.set_enabled(True)
        self._mixer.set_enabled(True)
        self._session_navigation.set_enabled(True)

    def _on_view_changed(self):
        view = self.application.view.focused_document_view
        is_arranger = (view == 'Arranger')

        # if is_arranger:
        #     self._enter_drum_mode()
        # else:
        self._enter_session_mode()

    # def _setup_clip_buttons(self):
    #     """Setup clip button listeners for hello world logging."""
    #     for track_idx in range(4):
    #         for scene_idx in range(4):
    #             button = self.elements.clip_buttons[track_idx][scene_idx]
    #             button.add_value_listener(
    #                 lambda value, t=track_idx, s=scene_idx: self._on_clip_button(value, t, s)
    #             )

    # def _setup_faders(self):
    #     """Setup fader listeners for hello world logging."""
    #     for track_idx in range(4):
    #         fader = self.elements.track_faders[0][track_idx]
    #         fader.add_value_listener(
    #             lambda value, t=track_idx: self._on_fader_change(value, t)
    #         )

    # def _setup_sends(self):
    #     """Setup send control listeners for hello world logging."""
    #     for track_idx in range(4):
    #         send = self.elements.send_controls[0][track_idx]
    #         send.add_value_listener(
    #             lambda value, t=track_idx: self._on_send_change(value, t)
    #         )

    # def _on_clip_button(self, value, track_idx, scene_idx):
    #     """Handle clip button press - hello world logging."""
    #     # if value > 0:
    #     #     self.log_message(f"Hello World: Clip button pressed - Track {track_idx}, Scene {scene_idx}")

    # def _on_fader_change(self, value, track_idx):
    #     """Handle fader change - hello world logging."""
    #     # self.log_message(f"Hello World: Fader {track_idx} changed to {value}")

    # def _on_send_change(self, value, track_idx):
    #     """Handle send change - hello world logging."""
    #     # self.log_message(f"Hello World: Send {track_idx} changed to {value}")

    def disconnect(self):
        super().disconnect()
        # self.log_message("Kontrol F1 disconnected")
