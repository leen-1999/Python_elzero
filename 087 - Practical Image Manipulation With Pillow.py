# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# -------------------------------------------------

from PIL import Image

# Open The Image
myImage = Image.open(
    "/Users/dunyakoyuncu/Documents/GitHub/Elzero_python/بلا عنوان/marguerite-729510_1280.webp")

# Show The Image
myImage.show()

# My Cropped Image
myBox = (300, 300, 800, 800)  # left, upper, right, lower
myNewImage = myImage.crop(myBox)

# Show The New Image
myNewImage.show()

# My Converted Mode Image
myConverted = myImage.convert("L")  # conver img to gray scale
myConverted.show()
