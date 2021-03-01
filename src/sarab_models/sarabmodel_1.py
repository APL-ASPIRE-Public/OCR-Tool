from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import tensorflow as tf
import os
import cv2
from PIL import Image
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from tensorflow.python.keras.layers.advanced_activations import ReLU

flipped = tf.image.flip_left_right(image)
visualize(image, flipped)


