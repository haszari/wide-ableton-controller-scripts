import colorsys
from ableton.v3.control_surface.components import ClipSlotComponent as BaseClipSlotComponent
from ableton.v3.control_surface.controls import ButtonControl
from ableton.v3.live.util import display_name


def liveobj_valid(obj):
    """Check if a Live object is valid (not None)."""
    return obj is not None


class KontrolF1ClipSlotComponent(BaseClipSlotComponent):
    """
    Custom ClipSlotComponent for Kontrol F1 with HSB color mode.
    
    Extracts actual clip colors from Ableton and converts to HSB mode
    for the Kontrol F1's RGB LED pads.
    """
    
    launch_button = ButtonControl()
    
    def _update_launch_button_color(self):
        """Override to send HSB colors based on actual clip color."""
        if not liveobj_valid(self._clip_slot):
            self._send_hsb_color(0, 0, 0)  # Black for no slot
            return
        
        # Determine the state and brightness level
        slot_or_clip = self._clip_slot.clip if self._has_clip() else self._clip_slot
        brightness_level = self._get_brightness_level(slot_or_clip)
        
        # Get the actual clip color
        if self._has_clip() and hasattr(slot_or_clip, 'color'):
            rgb_color = self._hex_to_rgb(slot_or_clip.color)
        else:
            rgb_color = (0, 0, 0)  # Black for empty slots
        
        # Convert RGB to HSB and send
        self._send_hsb_from_rgb(rgb_color, brightness_level)
    
    def _get_brightness_level(self, slot_or_clip):
        """Determine brightness level based on clip state."""
        if slot_or_clip.is_triggered:
            return 120  # Bright for triggered
        elif slot_or_clip.is_playing:
            return 80  # Mid for playing
        elif slot_or_clip.is_recording:
            return 80  # Mid for recording
        elif self._has_clip():
            return 40  # Dim for stopped clips
        else:
            return 0  # Off for empty slots
    
    def _hex_to_rgb(self, hex_value):
        """Convert hex color to RGB tuple (0-255)."""
        return ((hex_value & 16711680) >> 16, (hex_value & 65280) >> 8, hex_value & 255)
    
    def _send_hsb_from_rgb(self, rgb, brightness):
        """Convert RGB to HSB and send on MIDI channels 1-3."""
        r, g, b = rgb
        
        # Convert RGB to HSB (HSV in Python's colorsys)
        r_norm, g_norm, b_norm = r / 255.0, g / 255.0, b / 255.0
        h, s, v = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)
        
        # Convert to MIDI range (0-127)
        hue = int(h * 127)
        saturation = int(s * 127)
        
        # Send HSB values on channels 1, 2, 3
        self._send_hsb_color(hue, saturation, brightness)
    
    def _send_hsb_color(self, hue, saturation, brightness):
        """Send HSB color values on MIDI channels 1-3."""
        if self.launch_button.control_element:
            # Send on channel 1 (hue)
            self.launch_button.control_element.send_value(hue, channel=1)
            # Send on channel 2 (saturation)
            self.launch_button.control_element.send_value(saturation, channel=2)
            # Send on channel 3 (brightness)
            self.launch_button.control_element.send_value(brightness, channel=3)
