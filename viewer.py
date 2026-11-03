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

def fit_size(width: int, height: int, max_width: int, max_height: int) -> tuple[int, int]:
    """
    Largest size with the same aspect ratio that fits the limits
    """
    scale = min(max_width / width, max_height / height, 1.0)
    return max(1, round(width * scale)), max(1, round(height * scale))

class ProgressViewer:
    """
    - Shows `job.pixels`, scaled to the screen, and saves the result when done
    - Only the displayed copy is scaled
    - Job always works on the original full-resolution array, which is also what gets saved
    """
 
    def __init__(self, job: AveragingJob, output_path: Path):
        self.job = job
        self.output_path = output_path
 
        enable_dpi_awareness()
        self.root = tk.Tk()
        self.root.title("Image averager")
 
        height, width = job.pixels.shape[:2]
        self.display_size = fit_size(
            width,
            height,
            int(self.root.winfo_screenwidth() * SCREEN_MARGIN),
            int(self.root.winfo_screenheight() * SCREEN_MARGIN),
        )
 
        self.label = tk.Label(self.root, borderwidth=0)
        self.label.pack()
        self.photo = None
        self._redraw()
