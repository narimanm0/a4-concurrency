import os
import threading
import numpy as np
from averaging import average_rows
 
SINGLE = "S"
MULTI = "M"

def split_into_bands(height: int, size: int, parts: int) -> list[tuple[int, int]]:
    """
    - Split the image height into `parts` bands made of whole block rows
    - Every band starts on a multiple of `size`, so no block is shared between threads
    - Bands are as even as possible; empty bands are dropped.
    """
    # ceiling division
    block_rows = -(-height // size) 
    parts = max(1, min(parts, block_rows))
    base, extra = divmod(block_rows, parts)
 
    bands = []
    row = 0
    for index in range(parts):
        rows_here = base + (1 if index < extra else 0)
        start = row * size
        row += rows_here
        bands.append((start, min(row * size, height)))
    return bands
