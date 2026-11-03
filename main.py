import argparse
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageOps
from processor import MULTI, SINGLE, AveragingJob

OUTPUT_FILE = Path("result.jpg")
 
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="average the colors of square blocks of a JPEG image, showing progress"
    )
    parser.add_argument("file", type=Path, help="path to a .jpg image")
    parser.add_argument("size", type=int, help="side of the averaging square, in pixels")
    parser.add_argument(
        "mode",
        type=str.upper,
        choices=[SINGLE, MULTI],
        help="S = single thread, M = one thread per CPU core",
    )
    args = parser.parse_args()
 
    if args.size < 1:
        parser.error("square size must be a positive integer")
    if not args.file.is_file():
        parser.error(f"file not found: {args.file}")
    return args

def load_rgb(path: Path) -> np.ndarray:
    """
    - Load an image as an RGB uint8 array, honoring the camera's rotation flag
    """
    with Image.open(path) as image:
        return np.array(ImageOps.exif_transpose(image).convert("RGB"))

def main() -> int:
    args = parse_args()
    try:
        pixels = load_rgb(args.file)
    except OSError as error:
        print(f"Cannot open image: {error}", file=sys.stderr)
        return 1
 
    try:
        # imported late: needs Tkinter
        from viewer import ProgressViewer
    except ImportError as error:
        print(f"tkinter is required to show the window: {error}", file=sys.stderr)
        return 1
 
    job = AveragingJob(pixels, args.size, args.mode)
    ProgressViewer(job, OUTPUT_FILE).run()
    return 0

if __name__ == "__main__":
    sys.exit(main())
