from rembg import remove
from PIL import Image
import cv2
import numpy as np

# Load image
img = Image.open("source-photo.jpg")

# Remove background
img = remove(img)

# White background
bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
bg.paste(img, mask=img)

# Convert to grayscale
gray = cv2.cvtColor(np.array(bg), cv2.COLOR_RGBA2GRAY)

# Improve local contrast
clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8,8))
gray = clahe.apply(gray)

Image.fromarray(gray).save("source-prepped.png")

print("✅ source-prepped.png created")