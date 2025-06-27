# penguin
Input values of 1 or 0 in an 8 bit string, 8 times creating a cheeky fun bitmap output image.
# Penguin Bitmap Generator 🐧

Create a fun 8x8 pixel image using binary input!  
Enter 1s and 0s in 8 separate 8-bit strings to generate a cheeky bitmap-style output — like a pixelated penguin or your own custom shape.

This project uses Python and PIL (Pillow) to render and save a bitmap image from binary user input.

## Features
- 8x8 custom binary grid input (like old-school bitmaps)
- Saves output as a `.png` image
- Quick and fun visual feedback

## Example Input
01100110
01100110
00000000
00111100
01000010
10000001
01111110
00111100


## Example Output
🧊 → A lil’ penguin or whatever your binary soul desires.

## Requirements
- Python 3+
- Pillow (`pip install pillow`)

## How to Run
```bash
python penguin_bitmap.py
