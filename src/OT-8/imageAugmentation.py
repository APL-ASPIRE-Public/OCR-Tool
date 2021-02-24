from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
from tf_image.core.random import random_function
from tf_image.core.colors import rgb_shift, channel_drop
from tf_image.core.convert_type_decorator import convert_type

pd.options.display.max_rows = 10
pd.options.display.float_format = "{:.1f}".format

np.set_printoptions(linewidth = 200)

def load_image(filename):
    # load the image
	img = load_img(filename, color_mode="grayscale", target_size=(28, 28))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 1 channel
	#img = img.reshape(1, 28, 28, 1)
	# prepare pixel data
	img = img.astype('float32')
	img = img / 255.0
	return img

img1 = load_image('/Users/anumanl1/Downloads/five.jpg')


def my_func(arg):
    arg = tf.convert_to_tensor(arg, dtype=tf.float32)
    return arg

my_func(img1)

bright = tf.image.adjust_brightness(img1, delta = .1)
#bright = tf.image.adjust_brightness(img1, 0.4)

#tf.keras.preprocessing.image.save_img(
 #   '/Users/anumanl1/Downloads/five.jpg', bright, data_format=None, file_format=None, scale=True
#)
tf.keras.preprocessing.image.array_to_img(
    bright, data_format=None, scale=True, dtype=None
)
image = tf.keras.preprocessing.image.array_to_img(bright)