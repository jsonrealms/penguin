from PIL import Image

# 8x8 pixel binary image (0 = white, 1 = black)
# Create an empty 8x8 list
penguin_bitmap = []

print("Enter 8 rows of 8 binary digits (0 or 1), one row at a time:")

for i in range(8):
    while True:
        row_input = input(f"Row {i+1}: ")
        if len(row_input) == 8 and all(c in '01' for c in row_input):
            penguin_bitmap.append([int(c) for c in row_input])
            break
        else:
            print("Invalid input. Enter exactly 8 digits of 0 or 1.")

# At this point, penguin_bitmap is ready to use for the image

# Create the base image
img = Image.new('1', (8, 8))

# Fill pixels
for y in range(8):
    for x in range(8):
        img.putpixel((x, y), penguin_bitmap[y][x])

# Upscale for visibility
img_upscaled = img.resize((160, 160), Image.NEAREST)

# Save and preview
img_upscaled.save("penguin.bmp")
img_upscaled.show()