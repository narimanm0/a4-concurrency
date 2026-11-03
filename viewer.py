import sys
import tkinter as tk
from pathlib import Path
import numpy as np
from PIL import Image, ImageTk
from processor import AveragingJob

# how often the window redraws while processing
REFRESH_MS = 50
# time the untouched original stays visible
START_DELAY_MS = 1000
# fraction of the screen the window may occupy
SCREEN_MARGIN = 0.9

def enable_dpi_awareness() -> None:
    """
    On Windows, report real screen pixels instead of scaled ones
    """
    if sys.platform == "win32":
        try:
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except (AttributeError, OSError):
            pass
