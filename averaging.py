import numpy as np

def average_block(pixels: np.ndarray, top: int, left: int, size: int) -> None:
    """
    - Replace one square block of `pixels` (HxWx3, uint8) with its mean color
    - Blocks touching the right/bottom edge are smaller 
    - NumPy slicing clips them automatically, so the mean is taken over the pixels that exist
    """
    block = pixels[top:top + size, left:left + size]
    mean_color = block.reshape(-1, block.shape[-1]).mean(axis=0)
    block[:] = np.rint(mean_color).astype(np.uint8)

def average_rows(pixels: np.ndarray, first_row: int, last_row: int, size: int) -> None:
    """
    - Average every block whose top edge lies in [first_row, last_row)
    - Blocks are visited left-to-right, then top-to-bottom. `first_row` must be a multiple of `size` so that bands handled by different threads never overlap.
    """
    width = pixels.shape[1]
    for top in range(first_row, last_row, size):
        for left in range(0, width, size):
            average_block(pixels, top, left, size)
