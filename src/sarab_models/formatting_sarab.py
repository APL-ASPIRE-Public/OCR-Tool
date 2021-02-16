# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/171LfLaeecH035z3BbEdsnEcktajozf_e
"""

image = imread(image_filepath)
normalized_image = image / 255.0 # so you have a 0-1 range of values
if image_not_square:
# add padding values to the shorter side of the image in order to make it a square and not distort it when resized later
image = pad_image_to_square(image)
grayscale_image = image.dot([0.07, 0.72, 0.21]) # this takes an rgb image and converts it to grayscale
binary_image = threshold_image(grayscale_image) # a function that takes a grayscale image and converts the pixels to 0 or 1 based on wether they are > or < than 0.5
final_image = resize_image(image, (28, 28))