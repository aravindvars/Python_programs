import sys

from PIL import Image

images = []

for arg in sys.argv[1:]: #'1:' is used to tell the program that start from 1 in the argv list
  image = Image.open(arg)
  images.append(image)
  
images[0].save(
  "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)