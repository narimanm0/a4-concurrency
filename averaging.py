import numpy as np

def average_block(pixels: np.ndarray, top: int, left: int, size: int) -> None:
    """
    - Replace one square block of `pixels` (HxWx3, uint8) with its mean color.
    - Blocks touching the right/bottom edge are smaller 
    - NumPy slicing clips them automatically, so the mean is taken over the pixels that exist.
    """
    block = pixels[top:top + size, left:left + size]
    mean_color = block.reshape(-1, block.shape[-1]).mean(axis=0)
    block[:] = np.rint(mean_color).astype(np.uint8)
