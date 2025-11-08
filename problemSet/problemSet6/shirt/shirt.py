import sys
import os
from PIL import Image, ImageOps

# -------------------------
# 1. Validate command-line arguments
# -------------------------
if len(sys.argv) != 3:
    sys.exit("Usage: python shirt.py input output")

input_file = sys.argv[1]
output_file = sys.argv[2]

# Valid extensions
valid_exts = (".jpg", ".jpeg", ".png")

# Check extensions
if not input_file.lower().endswith(valid_exts) or not output_file.lower().endswith(valid_exts):
    sys.exit("Input and output must be JPEG or PNG files")

# Check matching extensions
if os.path.splitext(input_file)[1].lower() != os.path.splitext(output_file)[1].lower():
    sys.exit("Input and output must have the same extension")

# Check input file exists
if not os.path.exists(input_file):
    sys.exit(f"Could not read {input_file}")

# -------------------------
# 2. Open the input image
# -------------------------
input_image = Image.open(input_file)

# -------------------------
# 3. Open the shirt image
# -------------------------
shirt = Image.open("shirt.png")

# -------------------------
# 4. Resize and crop input to match shirt size
# -------------------------
input_resized = ImageOps.fit(input_image, shirt.size)

# -------------------------
# 5. Overlay the shirt (with transparency)
# -------------------------
input_resized.paste(shirt, (0, 0), shirt)  # the third argument ensures transparency

# -------------------------
# 6. Save the output
# -------------------------
input_resized.save(output_file)
