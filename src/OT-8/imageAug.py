from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
from matplotlib import pyplot as plt
import PIL
from PIL import Image, ImageEnhance

img = Image.open('/Users/anumanl1/Downloads/five.jpg')
enhancer = ImageEnhance.Brightness(img)
factor=4 
augmented_img = enhancer.enhance(factor)
augmented_img.save('/Users/anumanl1/Downloads/enhanced-image.jpg')





