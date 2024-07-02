"""
Image Resizer
by Wyatt Newell
7/2/2024

The following program is an image resizer. I had a recent problem which required such a program, and I wasn't all too thrilled with the options I had. 
I have not worked with image manipulation in python before, so this will offer a good learning opportunity. 

There are packages already available for such a project. This will help, however my end goal is for the user to have a simple GUI that will allow for input of an image,
resize options, and output path for said image. I would prefer the user not having to write within the python code itself. 
"""
from PIL import Image
import os

image_path = "c:/Users/tinyt/OneDrive/Desktop/100PythonProjects/4_ImageResizer/Checkmark.jpg"

# # PIL Test
if os.path.isfile(image_path):
    print("File Exists.")
else:
    print("File does not exist.")

try:
    img = Image.open(image_path)
    img.show()
    print("Image loaded successfully with PIL.")
except Exception as e:
    print(f"Error: {e}")