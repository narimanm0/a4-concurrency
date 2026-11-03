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
