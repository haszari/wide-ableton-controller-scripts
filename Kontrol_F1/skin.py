import colorsys
from ableton.v3.base import hex_to_rgb
from ableton.v3.control_surface.colors import BasicColors
from ableton.v3.control_surface.elements import ColorPart, ComplexColor, SimpleColor
from ableton.v3.control_surface.skin import Skin


class F1Color:
    """Kontrol F1 color with dim and bright MIDI values."""
    
    def __init__(self, base_midi, hue=0, saturation=1.0, brightness=0.5):
        self.hue = hue
        self.saturation = saturation
        self.brightness = brightness
        self.base_midi = base_midi
    
    @property
    def dim(self):
        """Dim brightness MIDI value."""
        return SimpleColor(self.base_midi, channel=12)
    
    @property
    def bright(self):
        """Bright brightness MIDI value (base + 2)."""
        return SimpleColor(self.base_midi + 2, channel=12)


class F1HSBColor:
    """
    Kontrol F1 HSB mode color.
    
    In HSB mode, color is set by sending three MIDI values on different channels:
    - Channel 1: hue (0-127)
    - Channel 2: saturation (0-127)
    - Channel 3: brightness (0-127)
    
    The note value targets the pad (same as pad note value).
    
    For multiple devices, use separate MIDI channels:
    - Device 1: channels 1-3
    - Device 2: channels 4-6
    - etc.
    """
    
    def __init__(self, r, g, b, brightness_level='mid', hue_channel=1, sat_channel=2, bright_channel=3):
        """
        Initialize HSB color from RGB values.
        
        Args:
            r, g, b: RGB values (0-255)
            brightness_level: 'dim' (40), 'mid' (80), or 'bright' (120)
            hue_channel: MIDI channel for hue (default 1)
            sat_channel: MIDI channel for saturation (default 2)
            bright_channel: MIDI channel for brightness (default 3)
        """
        # Convert RGB to HSB (HSV in Python's colorsys)
        r_norm, g_norm, b_norm = r / 255.0, g / 255.0, b / 255.0
        h, s, v = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)
        
        # Convert to MIDI range (0-127)
        self.hue = int(h * 127)
        self.saturation = int(s * 127)
        
        # Set brightness based on level
        brightness_levels = {'dim': 40, 'mid': 80, 'bright': 120}
        self.brightness = brightness_levels.get(brightness_level, 80)
        
        self.hue_channel = hue_channel
        self.sat_channel = sat_channel
        self.bright_channel = bright_channel
    
    def dim(self):
        """Return dim version of this color."""
        return F1HSBColor(
            int((self.hue / 127.0) * 255),
            int((self.saturation / 127.0) * 255),
            int((self.brightness / 127.0) * 255),
            brightness_level='dim',
            hue_channel=self.hue_channel,
            sat_channel=self.sat_channel,
            bright_channel=self.bright_channel
        )
    
    def mid(self):
        """Return mid brightness version of this color."""
        return F1HSBColor(
            int((self.hue / 127.0) * 255),
            int((self.saturation / 127.0) * 255),
            int((self.brightness / 127.0) * 255),
            brightness_level='mid',
            hue_channel=self.hue_channel,
            sat_channel=self.sat_channel,
            bright_channel=self.bright_channel
        )
    
    def bright(self):
        """Return bright version of this color."""
        return F1HSBColor(
            int((self.hue / 127.0) * 255),
            int((self.saturation / 127.0) * 255),
            int((self.brightness / 127.0) * 255),
            brightness_level='bright',
            hue_channel=self.hue_channel,
            sat_channel=self.sat_channel,
            bright_channel=self.bright_channel
        )
    
    def to_color(self):
        """Convert to ComplexColor for sending via MIDI."""
        return ComplexColor([
            ColorPart(self.hue, channel=self.hue_channel),
            ColorPart(self.saturation, channel=self.sat_channel),
            ColorPart(self.brightness, channel=self.bright_channel)
        ])


class F1IndexedColors:
    """Kontrol F1 indexed color palette from Native Instruments Controller Editor manual."""
    
    BLACK = F1Color(0, 0, 0.0, 0.0)
    WHITE = F1Color(72, 0, 1.0, 1.0)
    ULTRAWHITE = F1Color(76, 0, 1.0, 1.0)
    
    RED = F1Color(4, 0)
    ORANGE = F1Color(8, 15)
    LIGHTORANGE = F1Color(12, 35)
    WARMYELLOW = F1Color(16, 50)
    
    YELLOW = F1Color(20, 60)
    LIME = F1Color(24, 86)
    GREEN = F1Color(28, 120)
    MINT = F1Color(32, 159)
    
    CYAN = F1Color(36, 180)
    TURQUOISE = F1Color(40, 192)
    BLUE = F1Color(44, 229)
    PLUM = F1Color(48, 248)
    
    VIOLET = F1Color(52, 269)
    PURPLE = F1Color(56, 294)
    MAGENTA = F1Color(60, 300)
    FUCHSIA = F1Color(64, 328)
    
    # All colourful colors (no black/white) for hue matching
    ALL_COLORS = [
        RED, ORANGE, LIGHTORANGE, WARMYELLOW,
        YELLOW, LIME, GREEN, MINT,
        CYAN, TURQUOISE, BLUE, PLUM,
        VIOLET, PURPLE, MAGENTA, FUCHSIA
    ]
    
    @staticmethod
    def get_closest_color(hex_color):
        """
        Find the nearest F1 colour by hue from an Ableton clip color (hex).
        
        Args:
            hex_color: RGB hex value from Ableton clip.color
            
        Returns:
            F1Color object with the closest hue
        """
        # Convert hex to RGB
        r, g, b = hex_to_rgb(hex_color)
        
        # Convert RGB to HSB
        r_norm, g_norm, b_norm = r / 255.0, g / 255.0, b / 255.0
        h, s, v = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)
        hue = int(h * 360)
        
        # Check for black/white (low saturation or brightness)
        sat = int(s * 100)
        bright = int(v * 100)
        if sat < 10 and bright < 10:
            return F1IndexedColors.BLACK
        
        # Find nearest colour by hue
        closest = F1IndexedColors.BLACK
        hue_delta = 999
        for colour in F1IndexedColors.ALL_COLORS:
            hued = abs(hue - colour.hue)
            if hued < hue_delta:
                hue_delta = hued
                closest = colour
        
        return closest


class KontrolF1Colors:
    """Custom color scheme for Kontrol F1 to reflect session clip state."""
    
    class DefaultButton:
        On = BasicColors.ON
        Off = BasicColors.OFF
        Disabled = BasicColors.OFF

    class Session:
        """
        Session colors using indexed colour mode.
        
        Uses the F1IndexedColors palette with dim/bright brightness levels.
        Triggered states use bright white (ULTRAWHITE).
        
        Note: For dynamic color matching from Ableton clip colors, a custom
        ClipSlotComponent would be needed (similar to the HSB approach).
        """
        
        # Empty slot states
        Slot = F1IndexedColors.BLACK.dim  # Empty slot
        SlotRecordButton = F1IndexedColors.BLACK.dim  # Empty slot on armed track
        NoSlot = F1IndexedColors.BLACK.dim  # No slot available
        
        # Clip states
        ClipStopped = F1IndexedColors.GREEN.dim  # Clip exists but stopped (dim green)
        ClipTriggeredPlay = F1IndexedColors.ULTRAWHITE.bright  # Clip triggered to play (bright white)
        ClipTriggeredRecord = F1IndexedColors.ULTRAWHITE.bright  # Clip triggered to record (bright white)
        ClipPlaying = F1IndexedColors.GREEN.bright  # Clip playing (bright green)
        ClipRecording = F1IndexedColors.RED.bright  # Clip recording (bright red)
        
        # Scene states
        Scene = F1IndexedColors.BLACK.dim
        SceneTriggered = F1IndexedColors.ULTRAWHITE.bright
        NoScene = F1IndexedColors.BLACK.dim
        
        # Stop clip states
        StopClipTriggered = F1IndexedColors.ULTRAWHITE.bright
        StopClip = F1IndexedColors.BLACK.dim
        StopClipDisabled = F1IndexedColors.BLACK.dim
        StopAllClipsPressed = F1IndexedColors.ULTRAWHITE.bright
        StopAllClips = F1IndexedColors.BLACK.dim


kontrol_f1_skin = Skin(KontrolF1Colors)
