# Image Averager
 
Shows a JPEG image and progressively replaces every `(square size) x (square size)` with the average color of its pixels. The result is saved to `result.jpg` in the current directory.

## Requirements
 
- Python 3.9 or newer, with Tkinter
- Packages from `requirements.txt` (NumPy, Pillow)

## Setup
 
```
python -m pip install -r requirements.txt
```

## Usage
 
```
python main.py <file.jpg> <square_size> <S|M>
```
 
| Argument      | Meaning                                            |
|---------------|----------------------------------------------------|
| `file.jpg`    | path to the JPEG image                             |
| `square_size` | side of averaging square in pixels                 |
| `S` / `M`     | `S` = single thread, `M` = one thread per CPU core |
 
Example: `python main.py JH_profile.jpg 20 M`
 
The window first shows the original image, then the squares are averaged step by step. When processing finishes, `result.jpg` is written and the window stays open until you close it.
