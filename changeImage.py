#!/usr/bin/env python3

#Simple script to tranform images and save them in the new format
#resolution 600x400 and JPEG format. Reads and writes file to src
from PIL import Image
import PIL
import os

src = "/home/student-03-7ef7402584ed/supplier-data/images"
size = (600,400)

#function to change the resolution to 600x400 pixels and change the format to JPEG.
#takes file path to an image as argument and has no return
def transform_img(imf_path):
  with Image.open(os.path.join(src,imf_path)) as img:
    im = img.convert('RGB')
    im.thumbnail(size)
    base = os.path.splitext(imf_path)[0]
    im.save(os.path.join(src,base + '.jpeg'),"JPEG")

#loops through every image in src file path
for img in os.listdir(src):
  if img.endswith('.tiff') and not img.startswith('.'):    #ignores hidden files and files not ending in '.tiff'
    transform_img(img)
